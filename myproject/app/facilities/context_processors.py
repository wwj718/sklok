#coding=utf-8
'''
全局的context
在TEMPLATE_CONTEXT_PROCESSORS设置里指向它们就行
'''
from models import Facilities,FacCategories

def getcategories(request):
	categories = FacCategories.objects.all()
	return ({'categories_list':categories,})
