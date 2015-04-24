from django.db import models
from django.utils import timezone

class Event(models.Model):
	start_time = models.DateTimeField('start of event', default=timezone.now)
	end_time = models.DateTimeField('end time of event', default=timezone.now)
	name = models.CharField(max_length=300)
	fb_id = models.IntegerField(default=-1)

	def __str__(self):
		return self.event_name

class Vendor(models.Model):
	name = models.CharField(max_length=300)
	events = models.ManyToManyField(Event)	

	def __str__(self):
		return self.vendor_name
