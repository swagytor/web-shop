from django import forms

from catalog.models import Product, Version

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('date_of_creation', 'date_of_last_change',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_product_description(self):

        cleaned_data = self.cleaned_data.get('product_description')

        for forbidden_word in FORBIDDEN_WORDS:
            if forbidden_word.lower() in cleaned_data.lower():
                raise forms.ValidationError(f'В описании товара не должно содержаться слово "{forbidden_word}"')

        return cleaned_data

    def clean_product_name(self):
        cleaned_data = self.cleaned_data.get('product_name')

        for forbidden_word in FORBIDDEN_WORDS:
            if forbidden_word.lower() in cleaned_data.lower():
                raise forms.ValidationError(f'В названии товара не должно содержаться слово "{forbidden_word}"')

        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
