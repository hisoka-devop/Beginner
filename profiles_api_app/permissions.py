from rest_framework import permissions

class UserProfilePermissions(permissions.BasePermission):
    '''allow users to edit their profiles only'''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.id == request.user.id
