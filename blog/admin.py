from django.contrib import admin
from .models import Post, Comments, Category, CustomTag
from taggit.models import Tag

admin.site.unregister(Tag)

@admin.register(CustomTag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    ordering = ["name", "slug"]
    search_fields = ["name"]
    #prepopulated_fields = {"slug": ["name"]}

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('post',)
    exclude = ('parent', )

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    

