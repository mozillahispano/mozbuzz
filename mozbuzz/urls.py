from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^' + settings.URL_PREFIX + 'admin/', include(admin.site.urls)),
    url(r'^' + settings.URL_PREFIX, include('mozbuzz.buzz.urls')),
    url(r'^' + settings.URL_PREFIX + 'accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^' + settings.URL_PREFIX + 'accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
    url(r'^' + settings.URL_PREFIX + 'accounts/password_change/$', 'django.contrib.auth.views.password_change', {'template_name': 'password_change.html'}),
    url(r'^' + settings.URL_PREFIX + 'accounts/password_change_done/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'password_change_done.html'}),
    url(r'^' + settings.URL_PREFIX + 'browserid/', include('django_browserid.urls')),
)
