from django.contrib import admin
from apps.forumkg.models import Post, PostImage

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'price', 'publish', 'status',)
    list_filter = ('status', 'author', 'created_at', 'price', 'publish', )
    search_fields = ('title', 'description')
    prepopulated_fields = {'description': ('title', ), 'slug': ('title', )}
    ordering = ('status', 'publish', 'price')

admin.site.register(PostImage)




