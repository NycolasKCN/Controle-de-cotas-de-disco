from django_app import views
from django.conf.urls import patterns, url

urlpatterns = patterns("",
    url(views.index, name="index"))
