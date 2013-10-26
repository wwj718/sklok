from django.contrib import admin
from models import People


class PeopleAdmin(admin.ModelAdmin):
	list_display = ('categories', 'content', 'img','extra','pub_date')


admin.site.register(People,PeopleAdmin)