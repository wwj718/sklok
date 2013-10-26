#coding=utf-8
from django.conf.urls.defaults import patterns, url
from models import Research
from django.views.generic import date_based
from views import  get_by_id,show_all_research




research_list = {  
    "queryset"   : Research.objects.all(),  
    "date_field" : "pub_date",
    'allow_empty': True, 
    'extra_context': {}

} 


#begin with /newsevents/
urlpatterns = patterns('',
    #(r'^$', date_based.archive_index, news_info), #默认页面
    (r'^$',show_all_research ),    
    (r'^(?P<id>\d*)/$',get_by_id ),

)

