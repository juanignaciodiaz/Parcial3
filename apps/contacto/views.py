from django.shortcuts import render
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
 

# Create your views here.
def contacto(request):
    return render(request, 'pages/contacto.html')

def send_email(correoelectronico):
    context = {'correoelectronico': correoelectronico}

    template = get_template('pages/contacto.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Correo de solicitud de trabajo' ,
        'Solicitud de trabajo por parte de una persona que quiere dar aporte a la tienda',
        settings.EMAIL_HOST_USER,
        [correoelectronico]
    )

    email.attach_alternative(content, 'text/html')
    email.send()
    
def contacto(request):
    if request.method == 'POST':
        correoelectronico = request.POST.get('correoelectronico')

        send_email(correoelectronico)

    return render(request, 'pages/contacto.html', {})
   
 
