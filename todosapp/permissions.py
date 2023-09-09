from rest_framework import permissions


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow owners and admins to edit,
    but allow read-only access to others.
    """

    def has_permission(self, request, view):
        # Allow read-only access for all requests, including unauthenticated users.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user is authenticated to allow creation of tasks.
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow owners and admins only to edit tasks, but read-only access for others, even other users.
        if request.method in permissions.SAFE_METHODS:
            return True
            # if you want obj read-only access only for other signed-in users
            # return request.user.is_authenticated

        return request.user.is_staff or (request.user == obj.owner)
