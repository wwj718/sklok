#coding=utf-8
from django.shortcuts import render_to_response
from models import Announcement
from django.template import RequestContext
from django.shortcuts import get_object_or_404 

'''
def show_all_news(request): #包含分页功能
	list_items = News.objects.filter(categories='N')	
	variables = RequestContext(request,{'list_items':list_items})
	return render_to_response("Introduction.html",variables)    
'''
#分类取：
def get_by_id(request,id): #包含分页功能
	id=int(id)
	announcement = get_object_or_404(Announcement, pk=id)
	variables = RequestContext(request,{'announcement':announcement})
	return render_to_response("announcement_detail.html",variables)

