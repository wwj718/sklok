#coding=utf-8
from django.shortcuts import render_to_response
from models import Book
from django.template import RequestContext


def show_all_book(request): #包含分页功能
	list_items = Book.objects.order_by('id')	
	variables = RequestContext(request,{'list_items':list_items})
	return render_to_response("publications.html",variables)    
