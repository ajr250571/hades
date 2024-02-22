from django import forms
from core.erp.models import Category


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

        # def save(self, commit=True):
        #     data = {}
        #     form = super()
        #     try:
        #         if form.is_valid():
        #             form.save()
        #         else:
        #             data['error'] = form.errors
        #     except Exception as e:
        #         data['error'] = str(e)
        #     return data

        # labels = {
        #    'name': 'Nombre Categoría',
        #    'desc': 'Descripción Categoría',
        # }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el Nombre',
                }
            ),
            'desc': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese la Descripcion',
                    'rows': 5
                }
            )
        }
