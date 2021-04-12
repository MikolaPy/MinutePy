from django.contrib import admin
from django.urls import path,include 

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('',include('blog.urls')),     #main apps url 
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>',never_cache(serve)))
