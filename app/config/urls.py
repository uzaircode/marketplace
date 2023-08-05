from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from core.views import frontpage, about


urlpatterns = [
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
    path('', include('userprofile.urls')),
    path('', include('store.urls')),
    # path('', frontpage.as_view(), name='frontpage'),
    path('', frontpage, name='frontpage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
