from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Project, TeamMember
from .serializers import ProjectSerializer, ProjectCreateSerializer, TeamMemberSerializer, TeamMemberCreateSerializer
from core.permissions import IsProjectOwnerOrManager
from rest_framework.exceptions import NotFound

# Create your views here.

class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(team_members__user=self.request.user)

    def perform_create(self, serializer):
        project = serializer.save(created_by=self.request.user)
        TeamMember.objects.create(user=self.request.user, project=project, role='OWNER')
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProjectCreateSerializer
        return ProjectSerializer


class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectOwnerOrManager]


class TeamMemberListCreateView(generics.ListCreateAPIView):
    serializer_class = TeamMemberSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectOwnerOrManager]

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            raise NotFound("Project not found.")
        return TeamMember.objects.filter(project=project)
    
    def perform_create(self, serializer):
        project_id = self.kwargs['project_id']
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            raise NotFound("Project not found.")
        serializer.save(project=project)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TeamMemberCreateSerializer
        return TeamMemberSerializer


class TeamMemberRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeamMemberSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectOwnerOrManager]

    def get_object(self):
        project_id = self.kwargs['project_id']
        member_id = self.kwargs['member_id']
        try:
            return TeamMember.objects.get(project_id=project_id, id=member_id)
        except TeamMember.DoesNotExist:
            raise NotFound("Team member not found.")