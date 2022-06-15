from django.shortcuts import render
from django.views.generic import View

from account.models import Account


class MainView(View):
    template_name = 'index.html'
    my_account = Account.objects.first()

    def get(self, request, *args, **kwargs):
        context = {'my_account': self.my_account}
        return render(request, template_name=self.template_name, context=context)
