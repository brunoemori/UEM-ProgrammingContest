from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.problems),
    url(r'^yourarticles$', views.ownProblems),
    url(r'^otherarticles$', views.otherProblems),
]
