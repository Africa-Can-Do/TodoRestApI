from rest_framework import permissions

class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Authenticated users can see a list of the todos
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Authenticated users are given read permissions, but no write permissions
        # The methods in permissions.SAFE_METHODS(GET, HEAD, OPTIONS) don't allow for creating, updating or deleting a todo
        if request.method in permissions.SAFE_METHODS:
            return True  

        # Admin and creator of todo have full CRUD privileges
        return obj.user == request.user or request.user.is_staff
