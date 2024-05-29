from __future__ import annotations
import os
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


def avatar_image_path(instance: User, filename: str) -> str:
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.username)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/crew/", filename)


class User(AbstractUser):
    avatar = models.ImageField(null=True, upload_to=avatar_image_path)

    class Meta:
        ordering = ("username",)
    
    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return self.username
