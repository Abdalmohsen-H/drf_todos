import json

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator

# from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from .models import Task


@method_decorator(csrf_exempt, name="dispatch")
class TodosListView(APIView):
    """class based view to handle list view of todos"""

    def get(self, request):
        """Handle get request to get all todos"""
        tasks = Task.objects.all()
        tasksList = [{"id": task.id, "title": task.title} for task in tasks]
        return JsonResponse(tasksList, safe=False, status=200)

    def post(self, request):
        """Handle post request to add todo"""
        request_data = json.loads(request.body)
        my_title = request_data.get("title")

        if isinstance(my_title, str) is False:
            return JsonResponse({"Error": "title must be of type string"}, status=400)
        elif len(my_title) == 0:
            return JsonResponse({"Error": "title can't be empty string"}, status=400)
        elif my_title:
            task = Task.objects.create(title=my_title)
            return JsonResponse({"id": task.id, "title": task.title}, status=201)
        else:
            return JsonResponse({"Error": "title is required"}, status=400)


@method_decorator(csrf_exempt, name="dispatch")
class TodosDetailsView(APIView):
    """class based view to handle details view of on todo"""

    def get(self, request, pk):
        """Handle get request to get one todo by ID"""
        task = get_object_or_404(Task, pk=pk)
        return JsonResponse({"id": task.id, "title": task.title}, status=200)

    def put(self, request, pk):
        """Handle put request to update one todo by ID"""
        request_data = json.loads(request.body)
        my_title = request_data.get("title")
        task = get_object_or_404(Task, pk=pk)
        if isinstance(my_title, str) is False:
            return JsonResponse({"Error": "title must be of type string"}, status=400)
        elif my_title and len(my_title) == 0:
            return JsonResponse({"Error": "title can't be empty string"}, status=400)
        elif my_title:
            task.title = my_title
            task.save()
            return JsonResponse({"id": task.id, "title": task.title}, status=200)
        else:
            return JsonResponse({"Error": "title is required"}, status=400)

    def delete(self, request, pk):
        """Handle delete request to remove one todo by ID'"""
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return JsonResponse({"message": "Task deleted successfully."}, status=204)
