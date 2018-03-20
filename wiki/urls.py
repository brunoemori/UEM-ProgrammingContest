from django.conf.urls import url
from django.views.generic import ListView
from .models import Article
from . import views

urlpatterns = [
    url(r'^(\d+)$', views.getPage),
    url(r'^newpage$', views.newPage),
    url(r'^edit/(\d+)$', views.editPage)
]
