from django.conf.urls import patterns, url
from polls import views
from .views import AboutView

urlpatterns = patterns('',
    url(r'^$', views.add_model),
    url(r'^thanks',  AboutView.as_view()),
)