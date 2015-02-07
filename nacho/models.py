from django.db import models

# Create your models here.

class Restaurant(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	name = models.CharField(max_length="80")
	phone = models.CharField(max_length="15")
	address = models.CharField(max_length="200")
	city = models.CharField(max_length="80")
	stateProvince = models.CharField(max_length="80")
	zip = models.CharField(max_length="10")
	latitude = models.FloatField()
	longitude = models.FloatField()
	happyHourStart = models.DateTimeField()
	happyHourEnd = models.DateTimeField()

	class Meta:
		ordering = ('created',)
