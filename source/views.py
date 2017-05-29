# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic.edit import FormView

from source.forms import MachineForm
from source.models import Machine


@method_decorator(login_required, name='dispatch')
class MachineListView(generic.ListView):
    model = Machine
    template_name = 'general/table.html'
    name = _('machine list')


    def get_context_data(self, **kwargs):
        name = self.name



class MachinePageView(FormView):
    template_name = 'work/formset.html'
    form_class = MachineForm
    success_url = 'source/'

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(MachinePageView, self).dispatch(*args, **kwargs)
