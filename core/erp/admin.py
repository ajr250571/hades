from django.contrib import admin
from core.erp.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('name',)
    ordering = ('name',)
