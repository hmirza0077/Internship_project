from django.contrib import admin
from .models import Post, Comments, Category, Tags
from taggit.models import Tag
from  parler.admin import TranslatableAdmin

@admin.register(Tags)
class TagAdmin(TranslatableAdmin):
    list_display = ["name", "slug"]
    #ordering = ["name", "slug"]
    search_fields = ["name"]
    #prepopulated_fields = {"slug": ["name"]}

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('post',)
    exclude = ('parent', )

@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    list_display = ('title', 'slug',)

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('name', 'slug',)
    

