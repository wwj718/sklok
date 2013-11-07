#coding=utf-8
from django.db import models
from mezzanine.core.models import Displayable, RichText

#richtext
#建立图片文件夹

#就用blog吧差不多

class Announcement(RichText):	
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField(blank=True,null=True)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name_plural   = "Announcement"
