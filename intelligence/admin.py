from django.contrib import admin
from .models import Gang, GangMember, Incident, GangRelationship, CaseFile


@admin.register(Gang)
class GangAdmin(admin.ModelAdmin):
    list_display = ['name', 'tag', 'threat_level', 'member_count', 'is_active']
    list_filter = ['threat_level', 'is_active']
    search_fields = ['name', 'tag']


@admin.register(GangMember)
class GangMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'alias', 'gang', 'rank', 'status', 'threat_level']
    list_filter = ['gang', 'status', 'threat_level']
    search_fields = ['name', 'alias']


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ['title', 'incident_type', 'location', 'date_time', 'severity', 'status']
    list_filter = ['incident_type', 'severity', 'status']
    search_fields = ['title', 'location']
    date_hierarchy = 'date_time'


@admin.register(GangRelationship)
class GangRelationshipAdmin(admin.ModelAdmin):
    list_display = ['gang_1', 'relationship_type', 'gang_2']
    list_filter = ['relationship_type']


@admin.register(CaseFile)
class CaseFileAdmin(admin.ModelAdmin):
    list_display = ['case_number', 'title', 'priority', 'status', 'lead_agent', 'opened_date']
    list_filter = ['priority', 'status']
    search_fields = ['case_number', 'title']
    date_hierarchy = 'opened_date'

