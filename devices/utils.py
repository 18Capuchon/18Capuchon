import qrcode
from io import BytesIO
from django.core.files.base import ContentFile

def generate_device_qr(device_id: str):
    qr = qrcode.make(device_id)
    buffer = BytesIO()
    qr.save(buffer, format='PNG')
    return ContentFile(buffer.getvalue(), name=f'{device_id}.png')
