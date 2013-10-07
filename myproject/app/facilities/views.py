#coding=utf-8
from django.shortcuts import render_to_response
from models import Facilities,FacCategories
from django.template import RequestContext

def show_all_facilities(request): #包含分页功能,categories和categories_list实际上一样
	categories = FacCategories.objects.all()
	list_items = Facilities.objects.order_by('id')	
	variables = RequestContext(request,{'categories_list':categories,'list_items':list_items})
	return render_to_response("facilities.html",variables)    

#分类取：
def get_by_category(request,category): #包含分页功能
	categories = FacCategories.objects.all()
	list_items = FacCategories.objects.get(name=category).facilities_set.all()	
	#list_items = Facilities.objects.filter(categories=category)	
	variables = RequestContext(request,{'categories_list':categories,'list_items':list_items,'category':category})
	return render_to_response("facilities.html",variables)    