from rest_framework.permissions import BasePermission


class IsAnonymous(BasePermission):
    message = "Please log out to register new account"

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return True

        return False


class UserEquelProfile(BasePermission):
    message = "User haven't permission"
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user == obj:
            return True