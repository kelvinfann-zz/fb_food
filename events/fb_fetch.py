from urllib2 import urlopen
try: from simplejson import loads
except ImportError: from json import loads

APP_ID = '1829549720604413'
APP_SECRET = '1104f306c16d5bc27665e9faa6d1d265'
OFF_THE_GRID_EVENTS_URL = 'OffTheGridSF/events'
FACEBOOK_GRAPH_URL = 'graph.facebook.com'

ACCESS_TOKEN = 'access_token=' + APP_ID + '|' + APP_SECRET
PARAMETERS = '?' + ACCESS_TOKEN
FACEBOOK_GRAPH_URL = 'https://' + FACEBOOK_GRAPH_URL

ALL_EVENTS_URL = FACEBOOK_GRAPH_URL + '/' + OFF_THE_GRID_EVENTS_URL
ALL_EVENTS_URL += ('/' + PARAMETERS)

def get_upcoming_events():
	upcoming_events = loads(urlopen(ALL_EVENTS_URL).read())
	return upcoming_events

def get_event(id):
	if type(id) == type(int):
		id = str(id)
	event_url = FACEBOOK_GRAPH_URL + '/' + id + '/?' + ACCESS_TOKEN
	event_details = loads(urlopen(event_url).read())
	return event_details

def upcoming_events_parser(upcoming_events):
	if type(upcoming_events) == type(dict): 
		upcoming_events = upcoming_events["data"]
	for event_short in upcoming_events:
		event_full = get_event(event_short["id"])
		add_event(event_full)


