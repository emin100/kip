from django.conf.urls import url
from django.contrib.auth.views import LoginView

from accounts.views import LoginKIPView

urlpatterns = [
    url(r'$', LoginKIPView.as_view(), name='accounts'),
]
