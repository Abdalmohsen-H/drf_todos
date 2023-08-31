from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        "auth.User", related_name="created_tasks", on_delete=models.PROTECT
    )
    # models.PROTECT will perevent deletion of user if it is associated with any task
    # while models.CASCADE deletes all tasks associated with a user if this user is deleted

    updated_by = models.ForeignKey(
        "auth.User", related_name="updated_tasks", on_delete=models.PROTECT
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["created_at"]
