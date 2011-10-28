from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^mozbuzz/admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'mozbuzz.views.home', name='home'),
    # url(r'^mozbuzz/', include('mozbuzz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

)
