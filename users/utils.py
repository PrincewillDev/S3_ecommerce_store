import random
from django.core.mail import EmailMessage
from .models import User, OneTimePassword
from django.conf import settings

def generate_otp():
    otp=""
    for i in range(6):
        otp+=str(random.randint(0,9))
    return otp

def send_otp_code(email):
    Subject="One Time Password for Email Verification"
    otp_code=generate_otp()
    print(otp_code)
    user=User.objects.get(email=email)
    current_site="myAuth.com"
    email_body=f"Hi {user.firstname},\n\nYour OTP for email verification is {otp_code}. Please do not share this OTP with anyone.\n\nRegards,\nTeam myAuth"
    from_email=settings.DEFAULT_FROM_EMAIL

    OneTimePassword.objects.create(user=user, code=otp_code)

    send_email=EmailMessage(subject=Subject, body=email_body, from_email=from_email, to=[email])
    send_email.send(fail_silently=True)