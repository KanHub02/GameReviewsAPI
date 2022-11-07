from rest_framework.permissions import BasePermission


class IsAnonymous(BasePermission):
    message = "Please log out to register new account"


    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return False