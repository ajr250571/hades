from os import name
from django.urls import path

from core.erp.views.category.views import *


app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/data/', CategoryDatatable.as_view(), name='category_data'),

]
