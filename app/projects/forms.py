from django import forms
from django.db.models.functions import Lower

from .models import Tag


class TagForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tags = Tag.objects.all().order_by(Lower('name'))
        for tag in tags:
            self.fields[tag.name] = forms.BooleanField(label=tag.name, required=False)
