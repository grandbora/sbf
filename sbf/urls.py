from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^flat/$', 'flat.views.index'),
#    url(r'^flat/(?P<poll_id>\d+)/$', 'flat.views.detail'),
#    url(r'^flat/(?P<poll_id>\d+)/results/$', 'flat.views.results'),
#    url(r'^flat/(?P<poll_id>\d+)/vote/$', 'flat.views.vote'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'flat.views.intro')
)
