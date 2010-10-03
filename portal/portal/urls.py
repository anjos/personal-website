from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
import audit.urls
import djangoogle.urls
import bitrepo.urls
import flatties.urls
import djit.urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^google/', djangoogle.urls.namespaced),
    url(r'^git/', djit.urls.namespaced),
    url(r'^audit/', audit.urls.namespaced),
    url(r'^openid/', include('django_openid_auth.urls')),
    url(r'^pages/', flatties.urls.namespaced),
    url(r'^bt/', bitrepo.urls.namespaced),
    url(r'^robots.txt$', include('robots.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/(?P<packages>\S+?)/$', 
      'django.views.i18n.javascript_catalog'),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog'),
    url(r'^$', 'portal.views.index', name='site-index'),
    url(r'^login/$', 'portal.views.login', name='login'), 
    url(r'^logout/$', 'portal.views.logout', name='logout'),
    # url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', 
    #   {'sitemaps': sitemaps}),

    # Media serving
    url(r'^media/(?P<path>.*)$',
     'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT,
     'show_indexes': True},
     name='media',
     ), 
    )

