from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Project


class ProjectListView(ListView):
    model = Project
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
