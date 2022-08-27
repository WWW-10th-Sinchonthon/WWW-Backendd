from django.contrib import admin
from .models import User
from .models import Post
from .models import Scrap

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Scrap)