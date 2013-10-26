#coding=utf-8
from django.shortcuts import render_to_response
from models import Research
from django.template import RequestContext
from django.shortcuts import get_object_or_404 


def show_all_research(request): #包含分页功能
	list_items = Research.objects.all()
	variables = RequestContext(request,{'list_items':list_items})
	return render_to_response("research.html",variables)    

#分类取：
def get_by_id(request,id): #包含分页功能
	id=int(id)
	research = get_object_or_404(Research, pk=id)
	variables = RequestContext(request,{'research':research})
	return render_to_response("researchdetail.html",variables)

