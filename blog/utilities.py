from django.template.loader import render_to_string
from django.core.signing import Signer
from MinutePy.settings import ALLOWED_HOSTS

signer = Signer()

def send_activation(user):
    #to generate address need the domain on which site is located
    #and value that uniquely identifies the user
    host = 'http://localhost:5000'      #or local host for dev
    context = {'user':user,'host':host,'sign':signer.sign(user.username)} #create digitally signed 
    subject = 'activated user'
    body_text = render_to_string('email/activation_letter_body.txt',context)
    user.email_user(subject,body_text)
