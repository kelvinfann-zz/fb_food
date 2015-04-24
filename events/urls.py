from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^v/$', views.vendors, name='vendors'),
	url(r'^u/$', views.events, name='events'),
]
