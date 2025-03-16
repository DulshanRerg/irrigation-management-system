from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Custom user model that supports different roles.
    """
    ROLE_CHOICES = [
        ('farmer', 'Farmer'),
        ('agronomist', 'Agronomist'),
        ('admin', 'Administrator'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='farmer')
    
    def __str__(self):
        return f"{self.username} ({self.role})"