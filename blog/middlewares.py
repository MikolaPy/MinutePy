from .models import *

def post_context_processor(request):
    context = {}
    context['markers'] = Marker.objects.all()
    return context

