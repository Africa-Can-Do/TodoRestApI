from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def send_verification_email(user):
    subject = 'Verify Your Email'
    token = user.generate_verification_token()
    context = {
        'user': user,
        'verification_token': token,
    }
    html_message = render_to_string('verification_email.html', context)
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, settings.EMAIL_HOST_USER, [user.email], html_message=html_message)
