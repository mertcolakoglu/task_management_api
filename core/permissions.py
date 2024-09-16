from rest_framework import permissions

class IsProjectOwnerOrManager(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'project'):
            project = obj.project
        else:
            project = obj
        
        user_member = project.team_members.filter(user=request.user).first()
        if user_member:
            return user_member.role in ['OWNER', 'MANAGER']
        return False

class IsTeamMemberOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.project.team_members.filter(user=request.user).exists()

class IsAssignedOrCreatorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.task.assigned_to == request.user or obj.task.created_by == request.user
    
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user