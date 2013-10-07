from django.contrib import admin
from models import News


class NewsAdmin(admin.ModelAdmin):
	list_display = ('title','categories', 'content', 'summary','pub_date')


admin.site.register(News,NewsAdmin)