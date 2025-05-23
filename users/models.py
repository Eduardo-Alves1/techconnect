from django.contrib.auth.models import AnonymousUser, AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('professional', 'Professional'),
        ('recruiter','Recruiter'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='professional')