from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput (
            attrs={
            "class": "form-control",
            "placeholder": "Seu email"
            }
        )    
    )
    name = forms.CharField(
        required=True,
        widget=forms.TextInput (
            attrs={
            "class": "form-control",
            "placeholder": "Seu nome"
            }
        )
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Mensagem",
                "rows": "2",
                "columns": "10"
            }
        )
    )