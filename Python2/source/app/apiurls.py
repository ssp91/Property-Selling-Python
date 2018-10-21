from django.conf.urls import url
from django.urls import reverse_lazy

from app.api import (PropertyView)

urlpatterns = [
    url(r'^properties/$', PropertyView.as_view())
]