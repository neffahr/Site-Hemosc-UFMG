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
            ("FLORIANOPOLIS", "Florianópolis"),
            ("JOINVILLE", "Joinville"),
            ("BLUMENAU", "Blumenau"),
            ("CRICIUMA", "Criciúma"),
            ("LAGES", "Lages"),
            ("JOACABA", "Joaçaba"),
            ("CHAPECO", "Chapecó")
        ],
        widget=forms.Select(
            attrs={
                "class": "form-field form-login",
                "placeholder": "Selecione a Unidade"
            }
        )
    )

    