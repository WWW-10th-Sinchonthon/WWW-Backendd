from django import views
from django.urls import path, include
from .views import signup,login, home

urlpatterns = [
    path('signup/', signup, name= 'signup'),
    path('login/', login, name='login'),
    path('', home, name='home'),

]
