from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

#author, title, price, publisher, stock position,
@python_2_unicode_compatible
class book(models.Model):
	author=models.CharField(max_length=100)
	title=models.CharField(max_length=100)
	publisher=models.CharField(max_length=100)
	price=models.IntegerField(default=0)
	num_copies=models.IntegerField(default=0)
        def __str__(self):
	     return self.title
