from django.shortcuts import render, redirect
from apps.contactform.forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

# Create your views here.
def contact_send_email(request):
    if (request.method == "GET"):
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            send_mail("Duvida/Sugestão do site", message, email, ['ufmghemosc@gmail.com', email])
            return HttpResponseRedirect(request.path_info)

    return render(request, 'contact.html', {'form': form})