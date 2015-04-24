import datetime
from django.shortcuts import render
from django.http import HttpResponse

from .models import Event, Vendor
from .fb_fetch import update, get_recent_appearances
# Create your views here.

def index(request):
	context = {}
	return render(request, 'events/index.html', context)

def vendors(request):
	vendors = Vendor.objects.order_by('-freq')
	context = {
		'vendors': vendors,
	}
	return render(request, 'events/vendors.html', context)

def vendor(request, vendor_id):
	vendor = Vendor.objects.get(id=vendor_id)
	vendor_events = get_recent_appearances(vendor)
	context = {
		'vendor': vendor,
		'vendor_events': vendor_events,
	}
	return render(request, 'events/vendor.html', context)

def events(request):
	events = Event.objects.filter(start_time__gt=datetime.datetime.now()).order_by('start_time')
	context = {
		'events': events
	}		
	return render(request, 'events/events.html', context)

def event(request, event_id):
	event = Event.objects.get(id=event_id)
	event_date = event.start_time.date()
	event_vendors = event.vendor_set.all()
	context = {
		'event': event,
		'event_date': event_date,
		'event_vendors': event_vendors,
	}
	return render(request, 'events/event.html', context)

def get_events(request):
	is_updated = update()
	context = {
		'is_updated': is_updated
	}
	return render(request, 'events/is_updated.html', context)
