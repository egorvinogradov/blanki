#coding:utf8
from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('naoplatu.views',
    url(r'^$', 'naoplatu', name='blanki-naoplatu'),
)
