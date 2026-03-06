import uuid
from django.db import models
from django.contrib.auth.models import User

class Home(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        max_length=100
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="home",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name