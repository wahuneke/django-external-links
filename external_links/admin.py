# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from django.contrib import admin
from django.db.models import Count
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _

from external_links.models import LinkClick

class LinkClickAdmin(admin.ModelAdmin):
    search_fields = ('link', 'referer', 'ip_addr' )
    date_hierarchy = 'date'
    list_filter = ('site', )
    list_display = ('link', 'referer', 'ip_addr', 'date', 'time')

    change_list_template = 'external_links/change_list.html'

    def has_add_permission(self, request):
        return False

    def top_links(self, request):
        """
        This view shows the top clicked external links
        """
        context = {
            'objects': LinkClick.objects.values('link').annotate(Count('link')).order_by('-link__count'),
            'title': _('Top clicked links'),
            'app_label': self.model._meta.app_label,
            'model_label': self.model._meta.verbose_name_plural,
        }
        return render_to_response('external_links/top_links.html',
                                  context,
                                  context_instance=RequestContext(request))

    def get_urls(self):
        urls = super(LinkClickAdmin, self).get_urls()
        my_urls = patterns('',
            url(r'^top/$',
                self.admin_site.admin_view(self.top_links),
                name='external_link_top_clicks')
        )

        return my_urls + urls
admin.site.register(LinkClick, LinkClickAdmin)

