from django.db import models
from django.utils import timezone


class Post(models.Model):# 'models' module is just given by Django.
	author = models.ForeignKey('auth.user')
	title = models.CharField(max_length=200) # limitied text insertion, such as for title.
	text = models.TextField() # unlimited Text insertion.
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title