#coding=utf-8
from django.db import models
#from mezzanine.conf import settings
from mezzanine.core.models import RichText


class Book(RichText):
	name = models.CharField(max_length=100,null=True)
	pdffile = models.FileField(upload_to="Publications", blank=True)
	pub_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)

	class Meta:
		verbose_name_plural = "Publications"