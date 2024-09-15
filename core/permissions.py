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