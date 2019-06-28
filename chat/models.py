import uuid

from django.db import models
from django.contrib.auth.models import User


def deserialize_user(user):
    """Deserialize user instance to JSON."""
    return {
        'id': user.id, 'username': user.username, 'email': user.email,
        'first_name': user.first_name, 'last_name': user.last_name
    }


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, blank=True, null=True)
    # author_email = models.EmailField(max_length=100)
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
