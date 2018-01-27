from django.contrib import admin
from rango.models import Category, Page, UserProfile


admin.site.register(UserProfile)

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fieds = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
	fields = ['category','title', 'url']
	list_display = ('title', 'category', 'url')

admin.site.register(Page, PageAdmin)