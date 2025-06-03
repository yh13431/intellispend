import uuid
from django.contrib.auth.models import User
from django.db import models

class Goal(models.Model):
    goal_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)