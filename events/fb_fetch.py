import datetime
from urllib2 import urlopen
try: from simplejson import loads
except ImportError: from json import loads
from .models import Event, Vendor

APP_ID = '1829549720604413'
APP_SECRET = '1104f306c16d5bc27665e9faa6d1d265'
OFF_THE_GRID_EVENTS_URL = 'OffTheGridSF/events'
FACEBOOK_GRAPH_URL = 'graph.facebook.com'

ACCESS_TOKEN = 'access_token=' + APP_ID + '|' + APP_SECRET
PARAMETERS = '?' + ACCESS_TOKEN
FACEBOOK_GRAPH_URL = 'https://' + FACEBOOK_GRAPH_URL

ALL_EVENTS_URL = FACEBOOK_GRAPH_URL + '/' + OFF_THE_GRID_EVENTS_URL
ALL_EVENTS_URL += ('/' + PARAMETERS)

def update():
	upcoming_events = loads(urlopen(ALL_EVENTS_URL).read())
	return _update(upcoming_events)

def _update(upcoming_events):
	for fb_event_short in upcoming_events["data"]:
		add_event(get_event(fb_event_short["id"]))
	for vendor in Vendor.objects.all():
		vendor.freq = len(get_recent_appearances(vendor))
		vendor.save()
	return True	

def get_event(fb_id):
	if type(fb_id) == type(int):
		fb_id = str(fb_id)
	event_url = FACEBOOK_GRAPH_URL + '/' + fb_id + '/?' + ACCESS_TOKEN
	fb_event_details = loads(urlopen(event_url).read())
	return fb_event_details

def add_event(fb_event):
	same_event = Event.objects.all().filter(fb_id=fb_event["id"])
	if not same_event:
		new_event = Event(
			name=fb_event["name"][:300],
			fb_id=fb_event["id"],	
			start_time=fb_date_parser(fb_event["start_time"]),
			end_time=fb_date_parser(fb_event["end_time"]),
			)
		new_event.save()
		vendors = description_vendor_parser(fb_event["description"])
		if vendors != None:
			for vendor in vendors:
				add_vendor_event(vendor, new_event)	

def add_vendor_event(vendor, db_event):
	db_vendor = Vendor.objects.all().filter(name=vendor)
	if vendor == '': return
	if not db_vendor:
		db_vendor = Vendor(
				name=vendor,				
			)
		db_vendor.save()
	else:
		if len(db_vendor) > 1: raise Exception('Duplicate Vendor')
		db_vendor = db_vendor[0]
	db_vendor.events.add(db_event)
	db_vendor.save()

def description_vendor_parser(fb_event_description):
	n_description = fb_event_description.replace('\r\n', '\n').replace(' \n',
		'\n').replace('\n ', '\n').split(':\n')[1:]
	n_broke_description = [item.split('\n\n')[0].split('\n') for item in n_description]
	valid_vendor_list = list()
	for section in n_broke_description:
		if is_valid_vendor_list(section):
			valid_vendor_list += [section]
	if len(valid_vendor_list) != 1: return None
	return valid_vendor_list[0]			 

def is_valid_vendor_list(vendors_list, n=2, vendor_name_length=30):
	i = 0
	for vendor in vendors_list:
		if len(vendor) > vendor_name_length: 
			i+=1
	return i <= n

def fb_date_parser(fb_date):
	fb_date_split = fb_date.split('T')
	date_split, time_split = fb_date_split[0].split('-'), fb_date_split[1].split(':')
	year, month, day = int(date_split[0]), int(date_split[1]), int(date_split[2])
	hour, minute = int(time_split[0]), int(time_split[1])
	return datetime.datetime(year, month, day, hour=hour, minute=minute)

def get_recent_appearances(vendor, n=30):
	thirty_days_ago = datetime.datetime.now() + datetime.timedelta(-1*n)
	return vendor.events.filter(start_time__range=(thirty_days_ago, 
		datetime.datetime.now()))







