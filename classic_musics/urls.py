from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve as mediaserve
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('classic_music_app.urls')),
    # re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
            # mediaserve, {'document_root': settings.MEDIA_ROOT})
] 





if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
