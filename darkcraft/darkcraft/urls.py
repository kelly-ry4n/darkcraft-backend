from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'darkcraft.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','world_save.views.list_map_saves'),
    url(r'^save/$','world_save.views.save_form'),
    url(r'^save/([0-9]+)$', 'world_save.views.download_world'),
    url(r'^render_map/', 'map.views.render_map'),
    url(r'^admin/', include(admin.site.urls)),
)
