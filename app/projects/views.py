from django.db.models import ObjectDoesNotExist
from django.views.generic import ListView

from .forms import TagForm
from .models import Project, Tag


class ProjectListView(ListView):
    template_name = 'project-list.html'
    model = Project
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['projects'] = self.object_list
        context['tag_filter'] = TagForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = self.model.objects.all()
        filtered = self.request.GET.keys()

        tags = []
        for tag_name in filtered:
            try:
                tag = Tag.objects.get(name=tag_name)
            except ObjectDoesNotExist:
                pass
            else:
                tags.append(tag)

        if tags:
            queryset = self.model.objects.filter(
                tags__in=tags
            ).distinct('created')

        return queryset
