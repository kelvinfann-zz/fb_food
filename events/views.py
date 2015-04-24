from django.shortcuts import render
from django.http import HttpResponse

from .models import Event, Vendor
from .fb_fetch import get_upcoming_events, get_event 
# Create your views here.

def index(request):
	context = {}
	return render(request, 'events/index.html', context)

def vendors(request):
	vendors = Vendor.objects.order_by('name')
	context = {
		'vendors': vendors,
	}
	return render(request, 'events/vendors.html', context)

def events(request):
	events = Event.objects.order_by('date')
	context = {
		'events': events
	}		
	return render(request, 'events/events.html', context)
