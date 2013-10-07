#coding=utf-8
'''
全局的context
在TEMPLATE_CONTEXT_PROCESSORS设置里指向它们就行
'''
from models import Home


def gethome(request): #包含分页功能,categories和categories_list实际上一样
	try:
		home = Home.objects.all()[0]
	except:
		home = Home.objects.all()
	return  ({'home':home})

