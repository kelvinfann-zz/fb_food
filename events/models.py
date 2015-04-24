from django.db import models

class Event(models.Model):
	date = models.DateTimeField('date of event')
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.event_name

class Vendor(models.Model):
	name = models.CharField(max_length=300)
	events = models.ManyToManyField(Event)	

	def __str__(self):
		return self.vendor_name
