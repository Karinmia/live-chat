import uuid

from django.db import models
# from django.contrib.auth.models import User


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # author = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    # updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)