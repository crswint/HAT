from django.conf.urls import patterns, include, url
from apps.maps import views
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^maps/', include('apps.maps.urls', namespace='maps'))
)