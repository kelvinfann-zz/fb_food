from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^v/$', views.vendors, name='vendors'),
	url(r'^u/$', views.events, name='events'),
	url(r'^u/get/$', views.get_events, name='get_events'),
]

