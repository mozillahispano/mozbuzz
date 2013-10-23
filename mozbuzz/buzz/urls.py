from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'mozbuzz.buzz.views',
    url(r'^$', 'index', name="index"),
    url(r'^mention/create$', 'mention', name="create"),
    url(r'^mention/(?P<pk>\d+)$', 'mention_view', name="mention_view"),
    url(r'^mention/(?P<pk>\d+)/edit$', 'mention', name="edit"),
    url(r'^mention/(?P<mention>\d+)/followups/new$', 'followup', name="followup_new"),
    url(r'^followup/(?P<pk>\d+)/edit$', 'followup', name="followup_edit"),
    url(r'^product/(?P<product>[a-z\-]+)/queue$', 'queue', name="product_queue"),
    url(r'^queue$', 'queue', name="queue"),
    url(r'^queue/delete$', 'queue_del'),
    url(r'^queue/update$', 'update_queue', name="update_queue"),
    url(r'^source/(?P<source>.*).json$', 'source_json', name="source_json"),
    url(r'^proxy$', 'proxy', name="proxy"),
    url(r'^about$', 'about', name="about"),
    url(r'^$', 'index', name="gracefully_degrade"),

)
