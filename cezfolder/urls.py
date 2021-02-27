from django.contrib import admin
from django.urls import include, path, re_path
from textpages.views import index, detail_text_page
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from . import views
from django.contrib.sitemaps.views import sitemap
from cezfolder.views import sitemap_view
from cezfolder.sitemaps import CompanySitemap, TextPagesSitemap, StaticSitemap


sitemaps = {
    'companies': CompanySitemap,
    'textpages': TextPagesSitemap,
    'static': StaticSitemap,
}

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('search/', views.search_view, name='search'),
    path('company/', include(('company.urls', 'companies'), namespace='company')),
    path('contacts/', include('contacts.urls')),
    path('externallinks/', include('externallinks.urls')),
    path('faqs/', include('faqs.urls')),
    path('<str:slug>', detail_text_page, name='detail_text_page'),
    path('', index, name='index'),
    path('i18n/', include('django.conf.urls.i18n')),
    re_path(r'captcha/', include('captcha.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('sitemap/', sitemap_view, name='sitemap'),
    re_path(r'^sitemap\.xml/$', sitemap, {'sitemaps': sitemaps}, name='sitemaps'),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += re_path(r'^rosetta/', include('rosetta.urls')),
