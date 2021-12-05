from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from orange.views import index, detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orange/', index),
    path('orange/<int:pk>/', detail),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)),
]