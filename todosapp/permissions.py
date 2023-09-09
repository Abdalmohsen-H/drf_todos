from datetime import timedelta

from django.utils import timezone
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

        if request.user.is_staff:  # if request.user is an admin
            return True  # allow everything for object without time restrictions

        # owner only have 7 days to edit but could delete any time
        if request.user == obj.owner:
            # Check if the task's "created_at" date is within the last 7 days
            seven_days_ago = timezone.now() - timedelta(days=7)
            is_recently_created = obj.created_at >= seven_days_ago
            return is_recently_created or (request.method == "DELETE")

        else:
            return False  # restirct others from editing or deleting
