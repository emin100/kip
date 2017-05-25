# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accounts.forms import LoginForm


class LoginKIPView(LoginView):
    template_name = 'account/login.html'
    #
    # def __init__(self):
    #     self.template_name = self.template_namez
        # form_class = LoginForm
        #
        # def get(self, request, *args, **kwargs):
        #     return self.
        #
        # def post(self, request, *args, **kwargs):
        #     return HttpResponseRedirect(reverse('accounts'))
