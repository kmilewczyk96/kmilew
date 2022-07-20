from django.views.generic import ListView

from .forms import TagForm
from .models import Project, Tag


class ProjectListView(ListView):
    template_name = 'project-list.html'
    model = Project
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['projects'] = self.object_list
        context['tag_filter'] = TagForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = self.model.objects.all()
        filtered = self.request.GET.keys()
        if filtered:
            tags = []
            for tag_name in filtered:
                tags.append(Tag.objects.get(name=tag_name))

            queryset = queryset.filter(
                tags__in=tags
            ).distinct()
            queryset = queryset.order_by('-created')

        return queryset
