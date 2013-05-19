# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns

urlpatterns = patterns('external_links.views',
    url(r'^$',
        'external_link',
        name='external_link')
)
