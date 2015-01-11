from django.conf.urls import patterns, url
from EEtabel import views

urlpatterns = patterns('',
    url(r'^$', views.people),
)