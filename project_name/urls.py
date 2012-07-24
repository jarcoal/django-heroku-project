from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

#admin
from django.contrib import admin
admin.autodiscover()

#api
from tastypie.api import Api as API

v1 = API(api_name='v1')
#v1.register()

urlpatterns = patterns('',
	url('^api/', include(v1.urls)),
	
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	
	#robots
	url(r'^robots\.txt$', direct_to_template, { 'template': 'robots.txt', 'mimetype': 'text/plain' }), 
)
