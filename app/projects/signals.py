from django.db.models import Count
from django.db.models.signals import post_delete

from .models import Project, Tag


def check_tag_count(sender, instance, **kwargs):
    """Delete tags if the only project related to them was just deleted."""
    tags_with_counter = Tag.objects.annotate(Count('projects'))
    for tag in tags_with_counter:
        if tag.projects__count == 0:
            tag.delete()


post_delete.connect(receiver=check_tag_count, sender=Project)
