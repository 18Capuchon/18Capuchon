from django.contrib import admin
from .models import Device, Home
from users.models import Profile
from django.utils.safestring import mark_safe

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'model', 'firmware', 'status', 'owner')
    search_fields = ('device_id',)
    list_filter = ('status',)
    readonly_fields = ('qr_preview',)

    def qr_preview(self, obj):
        if obj.qr_code:
            return mark_safe(f'<img src="{obj.qr_code.url}" width="150" />')
        return "-"

    qr_preview.allow_tags = True
    qr_preview.short_description = "QR Code"

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'avatar')


