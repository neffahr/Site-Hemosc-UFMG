from django.urls import path
from apps.contactform.views import contact_send_email

urlpatterns = [
    path('contact/', contact_send_email, name='contact')
]