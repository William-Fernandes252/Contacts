from concurrent.futures import process
from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Category(models.Model):
    name = models.CharField(max_length=32)
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32, blank=True)
    phone = models.CharField(
        max_length=32, 
        validators=[
            RegexValidator(
                regex=r'^[0-9]{12,13}$', message="Invalid phone number. Must include country code and DDD."
            )
        ]
    )
    email = models.EmailField(
        max_length=255, 
        validators=[
            EmailValidator(message="Invalid email address.")
        ]
    )
    creation_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    show = models.BooleanField(default=True)
    picture = ProcessedImageField(
        blank=True, 
        upload_to='pictures/%Y/%m/%d', 
        processors=[
            ResizeToFill(400, 400)
        ],
        format='JPEG',
        options={'quality': 100}
    )
    
    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)
    
    @property
    def fullname(self):
        return f'{self.name} {self.surname}'
    
    def __str__(self):
        return self.name