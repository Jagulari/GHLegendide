from __future__ import unicode_literals
from django.db import models

class MyModel(models.Model):
	title = models.CharField(max_length=25, unique=True, error_messages={'unique':"See nimi on juba lisatud."})
	timestamp = models.DateTimeField()

	def __str__(self):
		return self.title