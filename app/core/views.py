import os

from random import shuffle

from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import View

from account.forms import ContactForm
from account.models import Account
from projects.models import Project


class MainView(View):
    template_name = 'index.html'
    form = ContactForm()

    def get(self, request, *args, **kwargs):
        my_account = Account.objects.get(owner__email=os.environ.get('ACCOUNT_OWNER'))
        project_showcase = Project.objects.filter(owner=my_account).filter(is_favourite=True)
        if len(project_showcase) > 3:
            project_showcase = list(project_showcase)
            shuffle(project_showcase)
            project_showcase = project_showcase[:3]

        context = {'my_account': my_account, 'showcase': project_showcase, 'form': self.form}
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        self.form = ContactForm(request.POST)
        if self.form.is_valid():
            message = self.form.save(commit=False)
            message.recipient = Account.objects.get(owner__email=os.environ.get('ACCOUNT_OWNER'))
            message.save()
            messages.success(request=request, message='Message sent successfully!')

            return redirect('home')
