#coding=utf-8
from django.shortcuts import render_to_response
from models import News
from django.template import RequestContext
from django.shortcuts import get_object_or_404 


def show_all_news(request): #包含分页功能
	list_items = News.objects.filter(categories='N')	
	variables = RequestContext(request,{'list_items':list_items})
	return render_to_response("Introduction.html",variables)    

#分类取：
def get_by_id(request,id): #包含分页功能
	id=int(id)
	new = get_object_or_404(News, pk=id)
	variables = RequestContext(request,{'new':new})
	return render_to_response("detail.html",variables)

def search_by_title(request):
	query=request.GET.get("title",'')
	news = News.objects.filter(title__icontains=query)
	variables = RequestContext(request,{'news':news})
	return render_to_response("research.html",variables)