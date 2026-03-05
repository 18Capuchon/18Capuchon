import uuid
import qrcode
from io import BytesIO
from django.core.files import File
from django.db import models
from django.contrib.auth.models import User


class Device(models.Model):

    STATUS_CHOICES = [
        ('new', 'New'),
        ('onboarding', 'Onboarding'),
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    device_id = models.CharField(
        max_length=64,
        unique=True,
        help_text="Unique ID from QR Code"
    )

    serial_number = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    home = models.ForeignKey(
        'Home',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="devices"
    )

    qr_code = models.ImageField(
        upload_to='device_qr/',
        blank=True,
        null=True
    )

    model = models.CharField(
        max_length=50,
        help_text="Device model"
    )

    firmware = models.CharField(
        max_length=20,
        help_text="Firmware version"
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='offline'
    )

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        creating = self._state.adding

        super().save(*args, **kwargs)

        if creating and not self.qr_code:
            qr = qrcode.make(self.device_id)
            buffer =BytesIO()
            qr.save(buffer, format='PNG')
            buffer.seek(0)

            self.qr_code.save(
                f'{self.device_id}.png',
                File(buffer),
                save=False
            )

            super().save(update_fields=["qr_code"])

    def __str__(self):
        return self.device_id

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
        related_name="home"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name