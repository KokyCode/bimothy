from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('gang-intelligence/', views.gang_intelligence, name='gang_intelligence'),
    path('member-profiles/', views.member_profiles, name='member_profiles'),
    path('territory-map/', views.territory_map, name='territory_map'),
    path('incident-reports/', views.incident_reports, name='incident_reports'),
    path('relationships/', views.relationships, name='relationships'),
    path('case-files/', views.case_files, name='case_files'),
    path('system-settings/', views.system_settings, name='system_settings'),
    
    # CRUD endpoints for edit mode
    path('api/gang/create/', views.create_gang, name='create_gang'),
    path('api/gang/<int:gang_id>/update/', views.update_gang, name='update_gang'),
    path('api/gang/<int:gang_id>/delete/', views.delete_gang, name='delete_gang'),
    
    path('api/member/create/', views.create_member, name='create_member'),
    path('api/member/<int:member_id>/update/', views.update_member, name='update_member'),
    path('api/member/<int:member_id>/delete/', views.delete_member, name='delete_member'),
    
    path('api/incident/create/', views.create_incident, name='create_incident'),
    path('api/incident/<int:incident_id>/update/', views.update_incident, name='update_incident'),
    path('api/incident/<int:incident_id>/delete/', views.delete_incident, name='delete_incident'),
    
    path('api/case/create/', views.create_case, name='create_case'),
    path('api/case/<int:case_id>/update/', views.update_case, name='update_case'),
    path('api/case/<int:case_id>/delete/', views.delete_case, name='delete_case'),
    
    path('api/relationship/create/', views.create_relationship, name='create_relationship'),
    path('api/relationship/<int:relationship_id>/update/', views.update_relationship, name='update_relationship'),
    path('api/relationship/<int:relationship_id>/delete/', views.delete_relationship, name='delete_relationship'),
]

