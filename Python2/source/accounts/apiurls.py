from django.conf.urls import url
from django.contrib.auth.views import (password_change, password_reset,
                                       password_reset_confirm)
from django.urls import reverse_lazy

from . import api

urlpatterns = [
    # url(r'^$', api.UserListView.as_view()),
    url(r'^login/$', api.LoginView.as_view()),
    # url(r'^logout/$', api.SignOut.as_view()),
]