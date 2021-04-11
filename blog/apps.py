from django.apps import AppConfig
from django.dispatch import Signal
from .utilities import send_activation  # this func send message act when registering


class BlogConfig(AppConfig):
    name = 'blog'


user_registered_signal = Signal(providing_args=['instance'])

def user_registered_dispatcher(sender,**kwargs):
    send_activation(kwargs['instance'])  # in template.py we send over signal user is instance 
                                            #AdvUser model than register
user_registered_signal.connect(user_registered_dispatcher)
