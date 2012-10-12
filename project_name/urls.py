# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

if 'rosetta' in settings.INSTALLED_APPS and settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )
