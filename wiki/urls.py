from django.conf.urls import url
from django.views.generic import ListView
from django.views.generic.base import RedirectView
from .models import Article
from . import views

urlpatterns = [
    url(r'^(\d+)$', views.getPage),
    url(r'^newpage$', views.newPage),
    url(r'^edit/(\d+)$', views.editPage),
    url(r'^delete/(\d+)$', views.deletePage),
    url(r'^$', RedirectView.as_view(url='/problems/', permanent=False))
]
