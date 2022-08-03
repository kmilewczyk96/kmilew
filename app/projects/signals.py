from django.db.models import Count
from django.db.models.signals import pre_delete

from .models import Project, Tag


def check_tag_count(sender, instance, **kwargs):
    project = instance
    tags_with_counter = Tag.objects.annotate(Count('projects'))
    project_tags = project.tags.all()
    for tag in tags_with_counter:
        if tag.projects__count == 1 and tag in project_tags:
            tag.delete()


pre_delete.connect(receiver=check_tag_count, sender=Project)
