from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Task
import json


@method_decorator(csrf_exempt, name='dispatch')
class Todos_list_view(View):
    ''' class based view to handle list view of todos '''

    def get(self, request):
        ''' Handle get request to get all todos '''
        tasks = Task.objects.all()
        tasksList = [{'id': task.id, 'title': task.title} for task in tasks]
        return JsonResponse(tasksList, safe=False, status=200)

    def post(self, request):
        ''' Handle post request to add todo'''
        request_data = json.loads(request.body)
        my_title = request_data.get('title')

        if my_title:
            task = Task.objects.create(title=my_title)
            return JsonResponse({'id': task.id, 'title': task.title}, status=201)
        else:
            return JsonResponse({'Error': "title is required"}, status=400)
