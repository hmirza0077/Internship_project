from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'size', 'gender', 'color', 'material', 'slug', 'price', 'is_available', 'created', 'updated']
    list_filter = ['is_available', 'created', 'updated']
    list_editable = ['price', 'is_available']
    prepopulated_fields = {'slug': ('name',)}