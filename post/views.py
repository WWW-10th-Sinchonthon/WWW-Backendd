#views
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Scrap

def home(request):
    return render(request, 'home.html')

def create(request):
    return render(request, 'create.html')

def createform(request):
    if request.method == 'POST':
        post = Post()
        post.image = request.POST['image']
        post.weather = request.POST['weather']
        post.weather_desc = request.POST['weather_desc']
        post.temp = request.POST['temp']
        post.temp_desc = request.POST['temp_desc']
        post.finedust =request.POST['finedust']
        post.finedust_desc =request.POST['finedust_desc']
        post.tmi =request.POST['tmi']
        post.wear_tag1 =request.POST['wear_tag1']
        post.wear_tag2 =request.POST['wear_tag2']
        post.wear_tag3 =request.POST['wear_tag3']
        post.today_tag1 =request.POST['today_tag1']
        post.today_tag2 =request.POST['today_tag2']
        post.today_tag3 =request.POST['today_tag3']
        post.user = request.user
        post.save()
    return redirect('home')


def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post_detail':post_detail})


def scrapview(request):
    pass
    