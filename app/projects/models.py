import os
import sys
import uuid

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models

from account.models import Account
from .utils import generate_thumbnail


def thumbnail_img_upload_path(_, filename):
    """Generate provisional file for project thumbnail."""
    return os.path.join('account', 'thumbnails', filename)


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=False, upload_to=thumbnail_img_upload_path)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    tags = models.ManyToManyField('Tag', related_name='projects')
    source_code = models.CharField(max_length=250, null=True, blank=True)
    demo = models.CharField(max_length=250, null=True, blank=True)
    is_favourite = models.BooleanField(default=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        output = generate_thumbnail(self.thumbnail)
        self.thumbnail = InMemoryUploadedFile(
            file=output,
            field_name='ImageField',
            name='project_thumbnail.png',
            content_type='img/png',
            size=sys.getsizeof(output),
            charset=None
        )
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']


class Tag(models.Model):
    WEIGHT = [
        (5, 'Backend programming language'),
        (4, 'Backend Framework'),
        (3, 'Frontend Framework'),
        (2, 'Frontend - js, css, html'),
        (1, 'Tools - docker etc.')
    ]
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=50)
    weight = models.IntegerField(choices=WEIGHT)

    class Meta:
        ordering = ['-weight', 'name']

    def __str__(self):
        return self.name
