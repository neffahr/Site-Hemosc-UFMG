from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput (
            attrs={
            "class": "form-field form-email",
            "placeholder": "Seu email"
            }
        )    
    )
    name = forms.CharField(
        required=True,
        widget=forms.TextInput (
            attrs={
            "class": "form-field form-name",
            "placeholder": "Seu nome"
            }
        )
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-field form-msg",
                "placeholder": "Mensagem",
                "rows": "2",
                "columns": "10"
            }
        )
    )