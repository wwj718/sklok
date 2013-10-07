#coding=utf-8
from django.db import models
from app.news.models import News

#顺序就按id吧，管理员遵守就行 约定
class 	Home(models.Model):
	announcement1 = models.CharField(max_length=100)
	announcement2 = models.CharField(max_length=100)
	news = models.ForeignKey(News)   
	#content = models.CharField(max_length=100,null=True)
	img1 = models.FileField(upload_to="Home", blank=True, help_text="686*268pix")
	img2 = models.FileField(upload_to="Home", blank=True, help_text="686*268pix")
	img3 = models.FileField(upload_to="Home", blank=True, help_text="686*268pix")
	img4 = models.FileField(upload_to="Home", blank=True, help_text="686*268pix")

	pub_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)