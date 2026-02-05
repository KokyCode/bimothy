from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Q
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Gang, GangMember, Incident, GangRelationship, CaseFile
from datetime import timedelta
from django.utils import timezone
import json


def login_view(request):
    """Login view for DOJ agents"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        agent_id = request.POST.get('agent_id')
        passcode = request.POST.get('passcode')
        
        user = authenticate(request, username=agent_id, password=passcode)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials. Access Denied.')
    
    return render(request, 'intelligence/login.html')


def logout_view(request):
    """Logout view"""
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('login')


@login_required
def dashboard(request):
    """Main dashboard view"""
    # Get statistics
    total_gangs = Gang.objects.filter(is_active=True).count()
    total_members = GangMember.objects.filter(status='ACTIVE').count()
    open_incidents = Incident.objects.filter(status__in=['OPEN', 'INVESTIGATING']).count()
    active_cases = CaseFile.objects.filter(status__in=['OPEN', 'ACTIVE']).count()
    
    # Recent incidents
    recent_incidents = Incident.objects.all()[:5]
    
    # High priority cases
    priority_cases = CaseFile.objects.filter(priority__in=['HIGH', 'URGENT'])[:5]
    
    # Critical gangs
    critical_gangs = Gang.objects.filter(threat_level='CRITICAL', is_active=True)[:5]
    
    context = {
        'total_gangs': total_gangs,
        'total_members': total_members,
        'open_incidents': open_incidents,
        'active_cases': active_cases,
        'recent_incidents': recent_incidents,
        'priority_cases': priority_cases,
        'critical_gangs': critical_gangs,
        'agent': request.user,
        'edit_mode': request.session.get('edit_mode', False),
    }
    
    return render(request, 'intelligence/dashboard.html', context)


@login_required
def gang_intelligence(request):
    """Gang intelligence view"""
    gangs = Gang.objects.filter(is_active=True).annotate(
        incident_count=Count('incidents')
    ).order_by('-threat_level', '-incident_count')
    
    context = {
        'gangs': gangs,
        'agent': request.user,
        'edit_mode': request.session.get('edit_mode', False),
    }
    
    return render(request, 'intelligence/gang_intelligence.html', context)


@login_required
def member_profiles(request):
    """Member profiles view"""
    members = GangMember.objects.filter(status='ACTIVE').select_related('gang')
    
    # Filter by gang if provided
    gang_filter = request.GET.get('gang')
    if gang_filter:
        members = members.filter(gang_id=gang_filter)
    
    # Filter by threat level
    threat_filter = request.GET.get('threat')
    if threat_filter:
        members = members.filter(threat_level=threat_filter)
    
    gangs = Gang.objects.filter(is_active=True)
    
    context = {
        'members': members,
        'gangs': gangs,
        'agent': request.user,
        'edit_mode': request.session.get('edit_mode', False),
    }
    
    return render(request, 'intelligence/member_profiles.html', context)


@login_required
def territory_map(request):
    """Territory map view"""
    gangs = Gang.objects.filter(is_active=True)
    
    context = {
        'gangs': gangs,
        'agent': request.user,
        'edit_mode': request.session.get('edit_mode', False),
    }
    
    return render(request, 'intelligence/territory_map.html', context)


@login_required
def incident_reports(request):
    """Incident reports view"""
    incidents = Incident.objects.all().prefetch_related('gangs_involved', 'members_involved')
    
    # Filters
    status_filter = request.GET.get('status')
    if status_filter:
        incidents = incidents.filter(status=status_filter)
    
    severity_filter = request.GET.get('severity')
    if severity_filter:
        incidents = incidents.filter(severity=severity_filter)
    
    context = {
        'incidents': incidents,
        'agent': request.user,
        'edit_mode': request.session.get('edit_mode', False),
    }
    
    return render(request, 'intelligence/incident_reports.html', context)


@login_required
def relationships(request):
    """Gang relationships view"""
    relationships = GangRelationship.objects.all().select_related('gang_1', 'gang_2')
    gangs = Gang.objects.filter(is_active=True)
    
    context = {
        'relationships': relationships,
        'gangs': gangs,
        'agent': request.user,
        'edit_mode': request.session.get('edit_mode', False),
    }
    
    return render(request, 'intelligence/relationships.html', context)


@login_required
def case_files(request):
    """Case files view"""
    cases = CaseFile.objects.all().select_related('lead_agent')
    
    # Filters
    status_filter = request.GET.get('status')
    if status_filter:
        cases = cases.filter(status=status_filter)
    
    priority_filter = request.GET.get('priority')
    if priority_filter:
        cases = cases.filter(priority=priority_filter)
    
    context = {
        'cases': cases,
        'agent': request.user,
        'edit_mode': request.session.get('edit_mode', False),
    }
    
    return render(request, 'intelligence/case_files.html', context)


@login_required
def system_settings(request):
    """System settings view"""
    if request.method == 'POST' and 'toggle_edit_mode' in request.POST:
        # Toggle edit mode in session
        edit_mode = request.session.get('edit_mode', False)
        request.session['edit_mode'] = not edit_mode
        messages.success(request, f'Edit mode {"enabled" if not edit_mode else "disabled"}')
        return redirect('system_settings')
    
    edit_mode = request.session.get('edit_mode', False)
    context = {
        'agent': request.user,
        'edit_mode': edit_mode,
    }
    
    return render(request, 'intelligence/system_settings.html', context)


# ===================================
# CRUD VIEWS FOR EDIT MODE
# ===================================

def check_edit_mode(request):
    """Helper to check if edit mode is enabled"""
    return request.session.get('edit_mode', False)


# Gang CRUD
@login_required
@require_http_methods(["POST"])
def create_gang(request):
    """Create a new gang"""
    if not check_edit_mode(request):
        return JsonResponse({'error': 'Edit mode not enabled'}, status=403)
    
    try:
        data = json.loads(request.body)
        gang = Gang.objects.create(
            name=data.get('name', ''),
            tag=data.get('tag', ''),
            color=data.get('color', '#FF0000'),
            territory=data.get('territory', ''),
            threat_level=data.get('threat_level', 'MEDIUM'),
            member_count=data.get('member_count', 0),
            description=data.get('description', ''),
            is_active=data.get('is_active', True)
        )
        return JsonResponse({'success': True, 'id': gang.id, 'message': 'Gang created successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@login_required
@require_http_methods(["POST"])
def update_gang(request, gang_id):
    """Update a gang"""
    if not check_edit_mode(request):
        return JsonResponse({'error': 'Edit mode not enabled'}, status=403)
    
    try:
        gang = get_object_or_404(Gang, id=gang_id)
        data = json.loads(request.body)
        
        for field in ['name', 'tag', 'color', 'territory', 'threat_level', 'description']:
            if field in data:
                setattr(gang, field, data[field])
        
        if 'member_count' in data:
            gang.member_count = int(data['member_count'])
        if 'is_active' in data:
            gang.is_active = bool(data['is_active'])
        
        gang.save()
        return JsonResponse({'success': True, 'message': 'Gang updated successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@login_required
@require_http_methods(["POST"])
def delete_gang(request, gang_id):
    """Delete a gang"""
    if not check_edit_mode(request):
        return JsonResponse({'error': 'Edit mode not enabled'}, status=403)
    
    try:
        gang = get_object_or_404(Gang, id=gang_id)
        gang.delete()
        return JsonResponse({'success': True, 'message': 'Gang deleted successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


# GangMember CRUD
@login_required
@require_http_methods(["POST"])
def create_member(request):
    """Create a new gang member"""
    if not check_edit_mode(request):
        return JsonResponse({'error': 'Edit mode not enabled'}, status=403)
    
    try:
        data = json.loads(request.body)
        gang = get_object_or_404(Gang, id=data.get('gang_id'))
        member = GangMember.objects.create(
            gang=gang,
            name=data.get('name', ''),
            alias=data.get('alias', ''),
            rank=data.get('rank', ''),
            threat_level=data.get('threat_level', 'LOW'),
            status=data.get('status', 'ACTIVE'),
            criminal_record=data.get('criminal_record', ''),
            notes=data.get('notes', '')
        )
        return JsonResponse({'success': True, 'id': member.id, 'message': 'Member created successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@login_required
@require_http_methods(["POST"])
def update_member(request, member_id):
    """Update a gang member"""
    if not check_edit_mode(request):
        return JsonResponse({'error': 'Edit mode not enabled'}, status=403)
    
    try:
        member = get_object_or_404(GangMember, id=member_id)
        data = json.loads(request.body)
        
        for field in ['name', 'alias', 'rank', 'threat_level', 'status', 'criminal_record', 'notes']:
            if field in data:
                setattr(member, field, data[field])
        
        if 'gang_id' in data:
            gang = get_object_or_404(Gang, id=data['gang_id'])
            member.gang = gang
        
        member.save()
        return JsonResponse({'success': True, 'message': 'Member updated successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@login_required
@require_http_methods(["POST"])
def delete_member(request, member_id):
    """Delete a gang member"""
    if not check_edit_mode(request):
        return JsonResponse({'error': 'Edit mode not enabled'}, status=403)
    
    try:
        member = get_object_or_404(GangMember, id=member_id)
        member.delete()
        return JsonResponse({'success': True, 'message': 'Member deleted successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


# Incident CRUD
@login_required
@require_http_methods(["POST"])
def create_incident(request):
    """Create a new incident"""
    if not check_edit_mode(request):
        return JsonResponse({'error': 'Edit mode not enabled'}, status=403)
    
    try:
        data = json.loads(request.body)
        incident = Incident.objects.create(
            title=data.get('title', ''),
            incident_type=data.get('incident_type', 'OTHER'),
            location=data.get('location', ''),
            description=data.get('description', ''),
            severity=data.get('severity', 'MEDIUM'),
            status=data.get('status', 'OPEN'),
            evidence=data.get('evidence', ''),
            reported_by=request.user
        )
        
        # Add gangs and members if provided
        if 'gang_ids' in data:
            incident.gangs_involved.set(data['gang_ids'])
        if 'member_ids' in data:
            incident.members_involved.set(data['member_ids'])
        
        return JsonResponse({'success': True, 'id': incident.id, 'message': 'Incident created successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@login_required
@require_http_methods(["POST"])
def update_incident(request, incident_id):
    """Update an incident"""
    if not check_edit_mode(request):
        return JsonResponse({'error': 'Edit mode not enabled'}, status=403)
    
    try:
        incident = get_object_or_404(Incident, id=incident_id)
        data = json.loads(request.body)
        
        for field in ['title', 'incident_type', 'location', 'description', 'severity', 'status', 'evidence']:
            if field in data:
                setattr(incident, field, data[field])
        
        if 'gang_ids' in data:
            incident.gangs_involved.set(data['gang_ids'])
        if 'member_ids' in data:
            incident.members_involved.set(data['member_ids'])
        
        incident.save()
        return JsonResponse({'success': True, 'message': 'Incident updated successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@login_required
@require_http_methods(["POST"])
def delete_incident(request, incident_id):
    """Delete an incident"""
    if not check_edit_mode(request):
        return JsonResponse({'error': 'Edit mode not enabled'}, status=403)
    
    try:
        incident = get_object_or_404(Incident, id=incident_id)
        incident.delete()
        return JsonResponse({'success': True, 'message': 'Incident deleted successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


# CaseFile CRUD
@login_required
@require_http_methods(["POST"])
def create_case(request):
    """Create a new case file"""
    if not check_edit_mode(request):
        return JsonResponse({'error': 'Edit mode not enabled'}, status=403)
    
    try:
        # Handle both JSON and form data (for file uploads)
        if request.content_type and 'multipart/form-data' in request.content_type:
            data = request.POST
            image = request.FILES.get('image')
        else:
            data = json.loads(request.body)
            image = None
        
        case = CaseFile.objects.create(
            case_number=data.get('case_number', ''),
            title=data.get('title', ''),
            description=data.get('description', ''),
            priority=data.get('priority', 'MEDIUM'),
            status=data.get('status', 'OPEN'),
            lead_agent=request.user,
            notes=data.get('notes', '')
        )
        
        # Handle image upload
        if image:
            case.image = image
            case.save()
        
        if 'gang_ids' in data:
            if isinstance(data.get('gang_ids'), str):
                gang_ids = [int(x) for x in data.get('gang_ids').split(',') if x]
            else:
                gang_ids = data.get('gang_ids', [])
            case.gangs.set(gang_ids)
        if 'member_ids' in data:
            if isinstance(data.get('member_ids'), str):
                member_ids = [int(x) for x in data.get('member_ids').split(',') if x]
            else:
                member_ids = data.get('member_ids', [])
            case.members.set(member_ids)
        
        return JsonResponse({'success': True, 'id': case.id, 'message': 'Case created successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@login_required
@require_http_methods(["POST"])
def update_case(request, case_id):
    """Update a case file"""
    if not check_edit_mode(request):
        return JsonResponse({'error': 'Edit mode not enabled'}, status=403)
    
    try:
        case = get_object_or_404(CaseFile, id=case_id)
        
        # Handle both JSON and form data (for file uploads)
        if request.content_type and 'multipart/form-data' in request.content_type:
            data = request.POST
            image = request.FILES.get('image')
        else:
            data = json.loads(request.body)
            image = None
        
        for field in ['case_number', 'title', 'description', 'priority', 'status', 'notes']:
            if field in data:
                setattr(case, field, data[field])
        
        # Handle image upload
        if image:
            case.image = image
        elif 'image' in data and data.get('image') == '':
            # Clear image if empty string is sent
            case.image = None
        
        if 'gang_ids' in data:
            if isinstance(data.get('gang_ids'), str):
                gang_ids = [int(x) for x in data.get('gang_ids').split(',') if x]
            else:
                gang_ids = data.get('gang_ids', [])
            case.gangs.set(gang_ids)
        if 'member_ids' in data:
            if isinstance(data.get('member_ids'), str):
                member_ids = [int(x) for x in data.get('member_ids').split(',') if x]
            else:
                member_ids = data.get('member_ids', [])
            case.members.set(member_ids)
        
        case.save()
        return JsonResponse({'success': True, 'message': 'Case updated successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@login_required
@require_http_methods(["POST"])
def delete_case(request, case_id):
    """Delete a case file"""
    if not check_edit_mode(request):
        return JsonResponse({'error': 'Edit mode not enabled'}, status=403)
    
    try:
        case = get_object_or_404(CaseFile, id=case_id)
        case.delete()
        return JsonResponse({'success': True, 'message': 'Case deleted successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


# GangRelationship CRUD
@login_required
@require_http_methods(["POST"])
def create_relationship(request):
    """Create a new gang relationship"""
    if not check_edit_mode(request):
        return JsonResponse({'error': 'Edit mode not enabled'}, status=403)
    
    try:
        data = json.loads(request.body)
        gang1 = get_object_or_404(Gang, id=data.get('gang_1_id'))
        gang2 = get_object_or_404(Gang, id=data.get('gang_2_id'))
        
        relationship = GangRelationship.objects.create(
            gang_1=gang1,
            gang_2=gang2,
            relationship_type=data.get('relationship_type', 'NEUTRAL'),
            notes=data.get('notes', '')
        )
        return JsonResponse({'success': True, 'id': relationship.id, 'message': 'Relationship created successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@login_required
@require_http_methods(["POST"])
def update_relationship(request, relationship_id):
    """Update a gang relationship"""
    if not check_edit_mode(request):
        return JsonResponse({'error': 'Edit mode not enabled'}, status=403)
    
    try:
        relationship = get_object_or_404(GangRelationship, id=relationship_id)
        data = json.loads(request.body)
        
        for field in ['relationship_type', 'notes']:
            if field in data:
                setattr(relationship, field, data[field])
        
        relationship.save()
        return JsonResponse({'success': True, 'message': 'Relationship updated successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@login_required
@require_http_methods(["POST"])
def delete_relationship(request, relationship_id):
    """Delete a gang relationship"""
    if not check_edit_mode(request):
        return JsonResponse({'error': 'Edit mode not enabled'}, status=403)
    
    try:
        relationship = get_object_or_404(GangRelationship, id=relationship_id)
        relationship.delete()
        return JsonResponse({'success': True, 'message': 'Relationship deleted successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

