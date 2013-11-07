from django.contrib import admin
from models import Facilities#,FacCategories


class FacilitiesAdmin(admin.ModelAdmin):
	list_display = ('categories', 'name', 'img','pub_date')


admin.site.register(Facilities,FacilitiesAdmin)
# admin.site.register(FacCategories)

#http://202.204.65.101/cms/
#http://laps.ncepu.edu.cn/
