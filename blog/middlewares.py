from .models import *

def post_context_processor(request):
    context = {}
    context['markers'] = Marker.objects.all()
    context['key'] = ''
    context['all'] = ''
    if 'key' in request.GET:
        key = request.GET['key']
        if key:
            context['key'] = '?key='+key
            context['all'] = context['key']
    if 'page' in request.GET:
        page = request.GET['page']
        if page != '1':
            if context['all']:
                context['all'] += '?page=' + page
            else:
                context['all'] = '?page=' + page
    return context
