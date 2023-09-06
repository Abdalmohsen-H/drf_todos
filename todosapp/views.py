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
