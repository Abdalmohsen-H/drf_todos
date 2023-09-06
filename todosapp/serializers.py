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
        # user must be user instance
        user = self.context["request"].user

        # Create a new Task instance with the owner and updated_by set to the current user
        task = Task.objects.create(
            owner=user,
            updated_by=user,
            **validated_data  # Any other validated data needed for Task creation
        )

        return task

    def update(self, instance, validated_data):
        """update the updated_by field only when an existing task
        is updated.
        instance here is an instance of the Task model"""
        instance.updated_by = self.context["request"].user

        instance.save()
        return instance
