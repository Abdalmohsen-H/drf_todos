from rest_framework import serializers

from .models import Task


class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "created_at", "updated_at"]
