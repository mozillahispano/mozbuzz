from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'buzz.views.index', name="index"),
    url(r'^mention/create$', 'buzz.views.mention', name="create"),
    url(r'^mention/(?P<pk>\d+)$', 'buzz.views.mention_view', name="mention_view"),
    url(r'^mention/(?P<pk>\d+)/edit$', 'buzz.views.mention', name="edit"),
    url(r'^mention/(?P<mention>\d+)/followups/new$', 'buzz.views.followup', name="followup_new"),
    url(r'^followup/(?P<pk>\d+)/edit$', 'buzz.views.followup', name="followup_edit"),
    url(r'^product/(?P<product>[a-z\-]+)/queue$', 'buzz.views.queue', name="product_queue"),
    url(r'^queue$', 'buzz.views.queue', name="queue"),
    url(r'^queue/delete$', 'buzz.views.queue_del'),
    url(r'^queue/update$', 'buzz.views.update_queue', name="update_queue"),
    url(r'^source/(?P<source>.*).json$', 'buzz.views.source_json', name="source_json"),
    url(r'^proxy$', 'buzz.views.proxy', name="proxy"),
    url(r'^about$', 'buzz.views.about', name="about"),
    url(r'^$', 'buzz.views.index', name="gracefully_degrade"),

)
