from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'activate', 'created', 'updated']
    list_filter = ['activate']
    search_fields = ['name', 'description']


admin.site.register(Category, CategoryAdmin)




