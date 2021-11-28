from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here.

def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #todo va bien
            email = EmailMessage (
                "EcoSabores: Nuevo Mensaje De Contacto",
                "Nombre: {} <{}>\n\nEscribio:\n\n{}".format(name, email,content),
                settings.EMAIL_HOST_USER,
                ['ecosaboreschile@gmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
                #todo ha ido bien
                return redirect(reverse('contact')+"?ok")
            except:
                #todo mal
                 return redirect(reverse('contact')+ "?fail")
           
    return render(request,'contact/contact.html', {'form': contact_form})