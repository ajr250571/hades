from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from core.erp.models import Category
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def category_list(request):
    data = {
        'title': 'Listado de Categorías',
        'categories': Category.objects.all()
    }

    return render(request, 'category/list.html', data)


class CategoryListView(ListView):
    model = Category
    template_name = "category/list.html"

    # @method_decorator(login_required)
    # @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # if request.method=="GET":
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {'name': 'Armando'}
        return JsonResponse(data)

    def get_queryset(self):
        # return Category.objects.filter(name__startswith="L")
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['object_list']=Category.objects.all()
        context["title"] = "Listado de Categorías"
        return context
