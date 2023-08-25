from django.contrib import admin

from catalog.models import Category, Product, Blog


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category_name')
    ordering = ('pk',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'product_category', 'product_price')
    list_filter = ('product_category',)
    search_fields = ('product_name', 'product_description',)
    ordering = ('pk',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    exclude = ('created_at', 'slug')
    list_display = ('pk', 'title', 'views_count', 'created_at', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title',)
    ordering = ('pk',)
