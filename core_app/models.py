from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=50, default="Bubby User")
    last_name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True, max_length=300)
    profile_image = models.ImageField(
        upload_to="profile_images", default="blank_user.png")

    def __str__(self):
        return self.user.username
