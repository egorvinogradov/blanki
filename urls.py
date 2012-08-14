from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.home', name='home'),
    url(r'^na-?oplatu/', include('naoplatu.urls')),
    url(r'^admin1254/', include(admin.site.urls)),
)
