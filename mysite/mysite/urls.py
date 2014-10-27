from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import hello, current_datetime, basicPage, blogPage, mbb342Page, latestEntries
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^blog/$', blogPage),
    url(r'^mbb342/$', mbb342Page),
    url(r'^$', basicPage),
    url(r'^test/$', latestEntries),
    

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
