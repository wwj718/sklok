#coding=utf-8
from django.shortcuts import render_to_response
from models import People
from django.template import RequestContext


def show_all_people(request): #包含分页功能
	list_items = People.objects.filter(categories='A')
	variables = RequestContext(request,{'list_items':list_items})
	return render_to_response("people.html",variables)    

#分类取：
def get_by_category(request,category): #包含分页功能
	#categories = People.objects.values("categories").distinct()
	list_items = People.objects.filter(categories=category)
	template="people.html"
	if category=='A':
		template="people_A.html"
	if category=='M':
		template="people_M.html"
	if category=='L':
		template="people_L.html"


	variables = RequestContext(request,{'categories':category,'list_items':list_items,'category':category})
	return render_to_response(template,variables)    