from rest_framework import permissions, viewsets

from .models import Task
from .serializers import TodoSerializer


class TodosViewSet(viewsets.ModelViewSet):
    """Viewset class to handle list (get all), create,
    retrieve (get one), update, partial update (HTTP PATCH method)
    and delete actions for todos"""

    queryset = Task.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """override the perform_create method to set
        the created_by and updated_by fields when a
        new task is created."""
        serializer.save(owner=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        """override the perform_update method to update
        the updated_by field only when an existing task
        is updated."""
        serializer.save(updated_by=self.request.user)
