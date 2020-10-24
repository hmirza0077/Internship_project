from django.contrib import admin
from .models import Category, Product
from  parler.admin import TranslatableAdmin

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):

    list_display = ['name', 'slug']
    # prepopulated_fields = {'slug': ('name',)}

    # def get_prepopulated_fields(self, request, obj=None):
    #     return {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(TranslatableAdmin):

    list_display = ['name', 'slug', 'size', 'price', 'is_available']
    list_filter = ['is_available', 'created', 'updated']
    list_editable = ['price', 'is_available']
    readonly_fields=('visit_num',)
    # prepopulated_fields = {'slug': ('name',)}

    # def get_prepopulated_fields(self, request, obj=None):
    #     return {'slug': ('name',)}