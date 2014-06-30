from django.conf.urls import patterns, url, include
from django.contrib import admin
import flatties.urls
import chords.urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^music/', chords.urls.namespaced),
    url(r'^openid/', include('django_openid_auth.urls')),
    url(r'^pages/', flatties.urls.namespaced),
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
    )

from django.conf import settings
if settings.DEBUG:

  # Media + Static serving
  urlpatterns += (

      url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True},
        name='media'),

      url('^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve'),

      )
