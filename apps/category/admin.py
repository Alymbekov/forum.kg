from django.contrib import admin
from apps.category.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    list_display_links = ('name', 'slug',)
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}
