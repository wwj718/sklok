#coding=utf-8
from django.db import models
#from mezzanine.conf import settings


class Book(models.Model):
	name = models.CharField(max_length=100,null=True)
	url = models.URLField(blank=True,null=True)
	editor= models.CharField(max_length=100,null=True)
	press= models.CharField(max_length=100,null=True)
	pub_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)