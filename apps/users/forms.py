from django import forms

class LoginForms(forms.Form):
    email=forms.CharField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-field login-field",
                "placeholder": "Email"
            }
        )
    )
    password=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-field login-field",
                "placeholder": "Senha"
            }
        )
    )

    