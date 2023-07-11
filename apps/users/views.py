from django.shortcuts import render, redirect
from apps.users.forms import LoginForms
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
            password=senha,
            location=location
        )
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'Bem vindo {email.split("@", 1)[0]}')
            return redirect('index')
        else:
            messages.error(request, 'Usuário/Senha/Unidade não correspondem')
            return redirect('login')
        
    return render(request, 'users/login.html', {'form': form})

def logout(request):
    if request.user.is_authenticated:    
        auth.logout(request)
        messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('index')