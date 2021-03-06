#coding=utf-8
from django.db import models
from mezzanine.core.models import Displayable, RichText

#richtext
#建立图片文件夹

#就用blog吧差不多

class News(RichText):
	CHOICES = (
		(u'N', u'News'),
		(u'E', u'Events'),
		
	)
	
	title = models.CharField(max_length=100)
	categories = models.CharField(max_length=50,null=True,choices=CHOICES)
	summary = models.CharField(max_length=200,null=True)#概要
	#pub_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
	pub_date = models.DateTimeField(blank=True,null=True)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name_plural   = "News"
