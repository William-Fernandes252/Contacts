from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=32)


class Contact(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32, blank=False)
    phone = models.CharField(
        max_length=32, 
        validators=[
            RegexValidator(
                regex=r'^[0-9]{2} [0-9]{1,2} [0-9]{9}', message="Invalid phone number. Must include country code and DDD."
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