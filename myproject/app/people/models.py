#coding=utf-8
from django.db import models
from mezzanine.core.models import RichText

#顺序就按id吧，管理员遵守就行 约定
class People(RichText):
	CHOICES = (
		(u'A', u'Academic committee'),
		(u'L', u'LAB Directors'),
		(u'M', u'Members'),
	)
	categories = models.CharField(max_length=50,null=True,choices=CHOICES)
	#content = models.CharField(max_length=100,null=True)
	img = models.FileField(upload_to="Facilities", blank=True, help_text="81*111pix")
	pub_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
	extra  = models.IntegerField(blank=True,null=True,default=0)