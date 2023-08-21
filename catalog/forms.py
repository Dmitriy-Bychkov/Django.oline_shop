from django import forms

from catalog.models import Product

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта',
                   'биржа', 'дешево', 'бесплатно', 'обман',
                   'полиция', 'радар'
                   ]


class ProductForm(forms.ModelForm):
    """Класс для генерации формы создания продукта"""

    class Meta:
        model = Product
        fields = "__all__"
        # fields = ('name', 'description', 'preview', 'price',)

    def clean(self):
        """Метод для валидации полей названия и описания продукта"""

        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        if name and any(word in name.lower() for word in FORBIDDEN_WORDS):
            self.add_error('name', 'Недопустимое слово в названии продукта!')

        if description and any(word in description.lower() for word in FORBIDDEN_WORDS):
            self.add_error('description', 'Недопустимое слово в описании продукта!')

        return cleaned_data
