from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
import qrcode
import uuid
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile

class Feature(models.Model):
    bus_number = models.CharField(max_length=10, default='TS08AA0000')
    bus_name = models.CharField(max_length=100, default='RTC')
    ticket_fare = models.DecimalField(max_digits=8, decimal_places=2, default=50)
    arrival_time = models.TextField(default='5.00')
    fromdesti = models.CharField(max_length=100, default=None)
    todesti = models.CharField(max_length=500, default=None)
    place_notes = models.TextField(blank=True, null=True, default="Interesting place to visit")
    bus_image = models.ImageField(upload_to='bus_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.bus_number} - {self.bus_name} - {self.fromdesti} - {self.todesti}'

class Confirmation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    from_location = models.CharField(max_length=255, null=True, blank=True)
    to_location = models.CharField(max_length=255, null=True, blank=True)
    passenger_name = models.CharField(max_length=255)
    email = models.EmailField()
    payment_mode = models.CharField(max_length=20, null=True, blank=True, default=1)
    booking_date = models.DateField(null=True, blank=True)
    qr_code = models.ImageField(upload_to='dummy_folder/',null=True, blank=True)
    
    def generate_qr_code(self, data):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        return img
    
    def  save_qr_code_to_database(self):
        if not self.qr_code:
            qr_data = f"From: {self.from_location}\nTo: {self.to_location}"
            qr_code_image = self.generate_qr_code(qr_data)

            # Create a BytesIO object
            buffer = BytesIO()

            # Save the QR code image to the BytesIO object
            qr_code_image.save(buffer, format='PNG')

            # Set the image field of the model using the BytesIO object
            self.qr_code.save(f"{self.id}_qr.png", SimpleUploadedFile(f"{self.id}_qr.png", buffer.getvalue()), save=False)

        
    def save(self, *args, **kwargs):
        self.save_qr_code_to_database()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.passenger_name}'s Booking"
