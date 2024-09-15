from rest_framework import serializers
from .models import Project, TeamMember
from users.serializers import UserSerializer

class TeamMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
   
    class Meta:
        model = TeamMember
        fields = ('id', 'user', 'role', 'joined_at')

class ProjectSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    team_members = TeamMemberSerializer(many = True, read_only = True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_by', 'created_at', 'updated_at', 'team_members')
    
class ProjectCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('name', 'description')
    
class TeamMemberCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['user', 'role']