from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":
        contactName = request.POST['contactName']
        contactEmail = request.POST['contactEmail']
        contactSubject = request.POST['contactSubject']
        contactMessage = request.POST['contactMessage']

        # send an email

        send_mail(
            'Message from: ' + contactName + ', subject: ' + contactSubject,  # subject
            contactMessage,  # message
            settings.EMAIL_HOST_USER,  # from email
            ['nsbrathwaite18@outlook.com'],  # to email
            fail_silently=False
        )

        return render(request, 'home.html', {'contactName': contactName})
    else:
        return render(request, 'home.html', {})
