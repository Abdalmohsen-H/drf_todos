from rest_framework import generics

from .models import Task
from .utils import TodosSerializer


class TodosListView(generics.ListCreateAPIView):
    """generic class based view to handle list view of todos"""

    queryset = Task.objects.all()
    serializer_class = TodosSerializer


class TodosDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """generic class based view to handle details view of one todo"""

    queryset = Task.objects.all()
    serializer_class = TodosSerializer
