from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Task, Comment

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    task = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'task', 'user', 'content', 'created_at']
        read_only_fields = ['user', 'task']

class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'project', 'assigned_to', 'created_by', 'status', 'priority', 'due_date', 'created_at', 'updated_at', 'comments']
        read_only_fields = ['created_by']