from django import forms

class LoginForms(forms.Form):
    email=forms.CharField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-field form-login",
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
                "class": "form-field form-login",
                "placeholder": "Senha"
            }
        )
    )
    location=forms.ChoiceField(
        label='Unidade',
        required=True,
        choices=[
            ("FLORIANÓPOLIS", "Florianópolis"),
            ("JOINVILLE", "Joinville"),
            ("BLUMENAU", "Blumenau"),
            ("CRICIÚMA", "Criciúma"),
            ("LAGES", "Lages"),
            ("JOAÇABA", "Joaçaba"),
            ("CHAPECÓ", "Chapecó")
        ],
        widget=forms.Select(
            attrs={
                "class": "form-field form-login",
                "placeholder": "Selecione a Unidade"
            }
        )
    )

    