from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'buzz.views.index', name="index"),
    url(r'^create$', 'buzz.views.create', name="create"),
    url(r'^mention/(?P<mention>\d+)/followups/new$', 'buzz.views.followup', name="followup_new"),
    url(r'^followup/(?P<pk>\d+)/edit$', 'buzz.views.followup', name="followup_edit"),
    url(r'^about$', 'buzz.views.about', name="about"),
)
