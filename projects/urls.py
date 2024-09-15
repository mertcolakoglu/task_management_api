from django.urls import path
from .views import (
    ProjectListCreateView,
    ProjectRetrieveUpdateDestroyView,
    TeamMemberListCreateView,
    TeamMemberRetrieveUpdateDestroyView
)

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),
    path('projects/<int:project_id>/members/', TeamMemberListCreateView.as_view(), name='team-member-list-create'),
    path('projects/<int:project_id>/members/<int:member_id>/', TeamMemberRetrieveUpdateDestroyView.as_view(), name='team-member-detail'),
]