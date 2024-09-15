from rest_framework import generics, permissions
from .models import Task, Comment
from .serializers import TaskSerializer, CommentSerializer
from core.permissions import IsTeamMemberOrReadOnly, IsAssignedOrCreatorOrReadOnly

# Create your views here.

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsTeamMemberOrReadOnly]

    def get_queryset(self):
        return Task.objects.filter(project__team_members__user = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)
    

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsTeamMemberOrReadOnly]


class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsTeamMemberOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(task_id=self.kwargs['task_id'], task__project__team_members__user=self.request.user)

    def perform_create(self, serializer):
        task = Task.objects.get(id=self.kwargs['task_id'])
        serializer.save(user=self.request.user, task=task)


class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAssignedOrCreatorOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(task_id=self.kwargs['task_id'], task__project__team_members__user=self.request.user)
