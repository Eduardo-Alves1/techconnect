from django.db import models
from users.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    specialties = models.CharField(max_length=255)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    experience = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)

