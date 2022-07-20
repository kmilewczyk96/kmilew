import uuid

from django.db import models

from account.models import Account


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=False)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    tags = models.ManyToManyField('Tag')
    is_favourite = models.BooleanField(default=False, null=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']


class Tag(models.Model):
    WEIGHT = [
        (5, 5),
        (4, 4),
        (3, 3),
        (2, 2),
        (1, 1)
    ]
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=50)
    weight = models.IntegerField(choices=WEIGHT)

    class Meta:
        ordering = ['-weight']

    def __str__(self):
        return self.name
