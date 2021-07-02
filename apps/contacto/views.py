from django.conf import settings
from django.shortcuts import render
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
        'Correo de solicitud de trabajo',
        'Formulario de contacto',
        settings.EMAIL_HOST_USER,
        [correoelectronico]
    )

    email.attach_alternative(content, 'text/html')
    email.send()
    
    
def contacto(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        telefono = request.POST.get('telefono')
        correoelectronico = request.POST.get('correoelectronico')
        cargo = request.POST.get('cargo')

        send_email(correoelectronico)

    return render(request, 'pages/contacto.html', {})
   
 
