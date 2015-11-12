from django.conf.urls import patterns, include, url
from addr.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mywork.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
        (r'^hello/$', hello),
        (r'^$',homepage),
        (r'^home/$',homepage), 
        (r'^delete/$',delete),
        (r'^search/$',search),
        (r'^more/$',more),
        (r'^addbook/$',addbook),
        (r'^submit/$',submit),
        (r'^submitauthor/$',submitauthor),
        (r'^addauthor/$',addauthor),
        (r'^deleteauthor/$',deleteauthor),
        (r'^authorlist/$',authorlist),
    url(r'^admin/', include(admin.site.urls)),
       
                
)
 