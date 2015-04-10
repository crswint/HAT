from django.conf.urls import patterns, include, url
from apps.maps import json_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'route', json_views.RouteCollection.as_view(), name='routes'),
    url(r'stop', json_views.StopCollection.as_view(), name='stops'),
    url(r'r1nstops', json_views.R1NStopCollection.as_view(), name='r1nstops'),
    url(r'r1sstops', json_views.R1SStopCollection.as_view(), name='r1sstops'),
    url(r'r2stops', json_views.R2StopCollection.as_view(), name='r2stops'),
    url(r'r3stops', json_views.R3StopCollection.as_view(), name='r3stops'),
    url(r'r4stops', json_views.R4StopCollection.as_view(), name='r4stops'),
    url(r'r5astops', json_views.R5AStopCollection.as_view(), name='r5astops'),
    url(r'r5bstops', json_views.R5BStopCollection.as_view(), name='r5bstops'),
    url(r'r6stops', json_views.R6StopCollection.as_view(), name='r6stops'),
)