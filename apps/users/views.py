from django.shortcuts import render, redirect
from apps.users.forms import LoginForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            email=form['email'].value()
            senha=form['password'].value()
            location=form['location'].value()

        user = auth.authenticate(
            request,
            username=email,
            password=senha

        )
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'Bem vindo {email}') # Strip @gmail part
            return redirect('index')
        else:
            messages.error(request, 'Usuário e/ou senha não correspondem') # implement messages
            return redirect('login')
        
    return render(request, 'users/login.html', {'form': form})
