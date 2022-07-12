from django.shortcuts import render
from django.views.generic import View

from account.models import Account
from projects.models import Project


class MainView(View):
    template_name = 'index.html'
    my_account = Account.objects.first()

    def get(self, request, *args, **kwargs):
        project_showcase = Project.objects.filter(owner=self.my_account).filter(is_favourite=True)
        context = {'my_account': self.my_account, 'showcase': project_showcase}
        return render(request, template_name=self.template_name, context=context)
