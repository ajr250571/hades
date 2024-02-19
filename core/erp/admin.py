from django.contrib import admin

from core.erp.models import *

# Register your models here.
admin.site.register(Category)

# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''
    list_display = ('id', 'name', 'cate', 'pvp',)
    list_filter = ('cate',)
    search_fields = ('name',)
    ordering = ('id',)


admin.site.register(Client)
