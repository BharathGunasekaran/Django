from django.contrib import admin # type: ignore
from .models import Post, Category, AboutUs

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title', 'content')
    list_filter = ('category', 'created_at')


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Post, PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(AboutUs)