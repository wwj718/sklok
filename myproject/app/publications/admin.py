from django.contrib import admin
from models import Book


class BookAdmin(admin.ModelAdmin):
	list_display = ('name','url', 'editor', 'press','pub_date')


admin.site.register(Book,BookAdmin)