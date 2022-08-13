from email.policy import default
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin = models.BooleanField('Admin', default=False)
    phone_number = models.CharField(max_length=20, blank=True)
    profile_image = models.ImageField(
        default='default.jpg',
        upload_to='profile_image',
        blank=True,
        validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )
    date_created = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    phone_number = models.CharField(max_length=20, blank=True)
    profile_image = models.ImageField(
        default='default.jpg',
        upload_to="profile_image",
        blank=True,
        validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )
    date_created = models.DateTimeField(auto_now_add=True)
