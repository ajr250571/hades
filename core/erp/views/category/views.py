from django.shortcuts import render
from core.erp.models import Category
from django.views.generic import ListView
from django_datatables_view.base_datatable_view import BaseDatatableView


def category_list(request):
    data = {
        'title': 'Listado de Categorias',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)


class CategoryListView(ListView):
    model = Category
    template_name = "category/list.html"

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de Categorias'
        return context


class CategoryDatatable(BaseDatatableView):
    model = Category
    columns = ['id', 'name']
    order_columns = ['id', 'name']
