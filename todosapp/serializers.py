from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class TodoSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    # ReadOnly Field : will be included when serializing a Task, but won't be
    # required when creating or updating a task, or will be ignored if provided.

    class Meta:
        model = Task
        fields = ["id", "title", "created_at", "updated_at", "owner", "updated_by"]

    def create(self, validated_data):
        """set the created_by and updated_by fields when a
        new task is created."""
        validated_data["owner"] = self.context["request"].user
        validated_data["updated_by"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """update the updated_by field only when an existing task
        is updated.
        instance here is an instance of the Task model"""
        instance.updated_by = self.context["request"].user

        instance.save()
        return instance
