from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Task(models.Model):
    class StatusChoice(models.TextChoices):
        PENDING = "Pending", "Pending"
        IN_PROGRESS = "In Progress", "In Progress"
        COMPLETE = "Complete", "Complete"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=StatusChoice.choices)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Task name : {self.name}, User: {self.user.username}"
