from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^flat/$', 'flat.views.index'),
    url(r'^flat/(?P<poll_id>\d+)/$', 'flat.views.detail'),
    url(r'^flat/(?P<poll_id>\d+)/results/$', 'flat.views.results'),
    url(r'^flat/(?P<poll_id>\d+)/vote/$', 'flat.views.vote'),
)