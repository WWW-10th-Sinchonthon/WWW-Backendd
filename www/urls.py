from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from post.views import *

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('detail/<int:post_id>', detail, name='detail'),
    path('accounts/', include('accounts.urls')),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



