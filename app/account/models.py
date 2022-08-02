import os.path
import uuid

from django.conf import settings
from django.db import models


def home_img_upload_path(_, filename):
    """Generate file for home profile pic."""
    extension = os.path.splitext(filename)[1]
    filename = 'home' + extension

    return os.path.join('account', filename)


class Account(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    position = models.CharField(max_length=48, null=False, blank=False)
    home_img = models.ImageField(null=True, blank=True, upload_to=home_img_upload_path)
    description = models.TextField(max_length=256, null=True, blank=True)
    link_github = models.CharField(max_length=128, null=True, blank=True)
    link_linkedin = models.CharField(max_length=128, null=True, blank=True)
    link_twitter = models.CharField(max_length=128, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.owner.email.split('@')[0]


class Message(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    recipient = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    sender_name = models.CharField(max_length=250)
    sender_email = models.EmailField(max_length=250)
    company = models.CharField(max_length=250, null=True, blank=True)
    message = models.TextField(max_length=2000)
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender_email

    class Meta:
        ordering = ['is_read', '-created']
