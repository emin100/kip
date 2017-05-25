# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages

# Create your views here.
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, FormView

from work.forms import FilesForm


class HomePageView(FormView):
    template_name = 'work/formset.html'
    form_class = FilesForm

    # def get_context_data(self, **kwargs):
    #     context = super(HomePageView, self).get_context_data(**kwargs)
    #     messages.info(self.request, 'hello http://example.com')
    #     return context