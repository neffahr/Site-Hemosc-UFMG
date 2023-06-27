from django import forms

class HemocentroForms(forms.Form):
    entry = forms.IntegerField(
        label='Entrada de Bolsas',
        required=True,
        widget=forms.NumberInput(
            attrs={
                "class": "form-field formdb",
            }
        )
    )
    exit = forms.IntegerField(
        label='Saída de Bolsas',
        required=True,
        widget=forms.NumberInput(
            attrs={
                "class": "form-field form-db",
            }
        )
    )
    total = forms.IntegerField(
        label='Quantidade Total',
        disabled=True,
        required=True,
        widget=forms.NumberInput(
            attrs={
                "class": "form-field form-db",
            }
        )
    )
