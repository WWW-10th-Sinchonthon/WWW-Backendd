from django import views
from django.urls import path, include
from .views import signup,login, home,edit

urlpatterns = [
    path('signup/', signup, name= 'signup'),
    path('login/', login, name='login'),
    path('edit/', edit, name='edit'),
    path('', home, name='home'),

]
