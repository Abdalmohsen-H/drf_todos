from rest_framework import viewsets

from .models import Task
from .utils import TodosSerializer


class TodosViewSet(viewsets.ModelViewSet):
    """Viewset class to handle list, create,
    retrieve, update, and delete actions for todos"""

    queryset = Task.objects.all()
    serializer_class = TodosSerializer
