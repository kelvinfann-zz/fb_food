from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^v/$', views.vendors, name='vendors'),
	url(r'^v/(?P<vendor_id>[0-9]+)/$', views.vendor, name='vendor'),
	url(r'^u/$', views.events, name='events'),
	url(r'^e/(?P<event_id>[0-9]+)/$', views.event, name='event'),
	url(r'^e/get/$', views.get_events, name='get_events'),
]

