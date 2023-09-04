from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class TodoSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    # ReadOnly Field : will be included when serializing a Task, but won't be
    # required when creating or updating a task, or will be ignored if provided.

    class Meta:
        model = Task
        fields = ["id", "title", "created_at", "updated_at", "owner", "updated_by"]
