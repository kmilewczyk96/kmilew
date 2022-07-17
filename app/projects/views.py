from django.db.models import ObjectDoesNotExist
from django.views.generic import ListView

from .models import Project, Tag


class ProjectListView(ListView):
    template_name = 'project-list.html'
    model = Project
    paginate_by = 9

    def get_queryset(self):
        search_query = self.request.GET.get('search_query')
        object_list = self.model.objects.all()

        if search_query:
            tech_list = search_query.split(',')
            tags = []
            for tech in tech_list:
                try:
                    tag = Tag.objects.get(name__icontains=tech.strip())
                except ObjectDoesNotExist:
                    pass
                else:
                    tags.append(tag)

            object_list = object_list.distinct().filter(
                tags__in=tags
            )

        return object_list
