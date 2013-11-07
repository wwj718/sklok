from django.contrib import admin
from models import Home


class HomeAdmin(admin.ModelAdmin):
	list_display = ('pub_date','announcement1', 'announcement2','img1','img2','img3','img4')


admin.site.register(Home,HomeAdmin)