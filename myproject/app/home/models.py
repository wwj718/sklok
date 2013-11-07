#coding=utf-8
from django.db import models
from app.news.models import News
from app.announcement.models import Announcement

#顺序就按id吧，管理员遵守就行 约定
class 	Home(models.Model):
	# announcement1 = models.CharField(max_length=100)
	# announcement2 = models.CharField(max_length=100)
	announcement1 = models.ForeignKey(Announcement,related_name='announcement1')  
	announcement2 = models.ForeignKey(Announcement,related_name='announcement2')  
	news = models.ForeignKey(News)  
	news_img =  models.FileField(upload_to="Home", blank=True,null=True, help_text="247*247pix")

	#content = models.CharField(max_length=100,null=True)
	img1 = models.FileField(upload_to="Home", blank=True, help_text="686*268pix")
	img2 = models.FileField(upload_to="Home", blank=True, help_text="686*268pix")
	img3 = models.FileField(upload_to="Home", blank=True, help_text="686*268pix")
	img4 = models.FileField(upload_to="Home", blank=True, help_text="686*268pix")

	pub_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)

	class Meta:
		verbose_name_plural = "Home"
		ordering = ['-id']
