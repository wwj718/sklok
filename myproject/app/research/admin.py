from django.contrib import admin
from models import Research


class ResearchAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'summary','pub_date')


admin.site.register(Research,ResearchAdmin)