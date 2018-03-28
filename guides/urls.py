from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^n1$', views.n1),
    url(r'^n2$', views.n2),
    url(r'^n3$', views.n3),
    url(r'^n4$', views.n4)
]
