#coding=utf-8
from django.conf.urls.defaults import patterns
from views import  get_by_id







#begin with /newsevents/
urlpatterns = patterns('',
    #(r'^$', date_based.archive_index, news_info), #默认页面
    # (r'^$',show_all_research ),    
    (r'^(?P<id>\d*)/$',get_by_id ),

)