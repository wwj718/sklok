#coding=utf-8
from django.db import models

class FacCategories(models.Model):
    name = models.CharField(max_length=50,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.name

	class Meta:
		verbose_name_plural = "FacCategories"

class Facilities(models.Model):
	categories = models.ForeignKey(FacCategories)   
	name = models.CharField(max_length=100,null=True)
	img = models.FileField(upload_to="Facilities", blank=True, help_text="235*154pix")
	pub_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)


	class Meta:
		verbose_name_plural = "Facilities"