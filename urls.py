from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^polls/', include('polls.urls')),
    url(r'^EEtabel/', include('EEtabel.urls')),
)