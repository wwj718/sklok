#coding=utf-8
from django.shortcuts import render_to_response
from models import Home
from django.template import RequestContext

def home(request): #包含分页功能,categories和categories_list实际上一样
	try:
		home = Home.objects.all()[0]
	except:
		home = Home.objects.all()
	variables = RequestContext(request,{'home':home})
	return render_to_response("home.html",variables)    

