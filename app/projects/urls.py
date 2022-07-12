from django.urls import path

from .views import ProjectListView


urlpatterns = [
    path('', ProjectListView.as_view(template_name='project-list.html'), name='project-list')
]
