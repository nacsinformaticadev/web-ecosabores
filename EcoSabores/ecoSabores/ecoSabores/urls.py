from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    # Path del cores
    path('',include('core.urls')),
    # Path del services
    path('services/',include('services.urls')),
    # Path del blog
    path('blog/',include('blog.urls')),
    # Path del Page
    path('page/',include('pages.urls')),
    # Path del Contact
    path('contact/',include('contact.urls')),
    # Path del admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#custom titles for admin pages
admin.site.site_header = 'EcoSabores'
admin.site.index_title = "Panel Administrador EcoSabores"
admin.site.site_title = 'EcoSabores'