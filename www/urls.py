from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from post.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('create/', create, name='create')

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
