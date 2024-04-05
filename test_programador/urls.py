from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from test_programador.settings import STATIC_ROOT, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),

    # Archivos en DEBUG False
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
]
