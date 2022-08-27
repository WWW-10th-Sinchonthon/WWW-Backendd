from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# class User(models.Model):
#     user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     nickname=models.CharField(max_length=30)
#     user_image=models.ImageField(upload_to='media', null=True, blank=True)
#     intro=models.TextField(null=True, blank=True)

#     def __str__(self):
#         return self.nickname

class Post(models.Model):
    image=models.ImageField(upload_to='media', null=True, blank=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    WEATHER_CHOICES = (
        ('0', '#맑음'),
        ('1', '#흐림'),
        ('2', '#비'),
        ('3', '#눈'),
        ('4', '#바람'),
    )
    weather=models.IntegerField(default=0, choices=WEATHER_CHOICES)
    temp=models.CharField(max_length=5)
    FINEDUST_CHOICES = (
        ('0', '#좋음'),
        ('1', '#조금좋음'),
        ('2', '#보통'),
        ('3', '#조금나쁨'),
        ('4', '#나쁨'),
    )
    finedust=models.IntegerField(default=0, choices=FINEDUST_CHOICES)
    tmi=models.TextField(null=True, blank=True)
    liked=models.IntegerField(null=True, blank=True)
    scrap=models.IntegerField(null=True, blank=True)
    wear_tag1=models.CharField(max_length=10)
    wear_tag2=models.CharField(max_length=10, null=True, blank=True)
    wear_tag3=models.CharField(max_length=10, null=True, blank=True)
    weather_tag1=models.CharField(max_length=10)
    weather_tag2=models.CharField(max_length=10, null=True, blank=True)
    weather_tag3=models.CharField(max_length=10, null=True, blank=True)

class Scrap(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='scrap_user')
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='scrap_post')

