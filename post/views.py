from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Scrap
from accounts.models import Users
from datetime import timedelta,date

def home(request):
    return render(request, 'Main.html')

def create(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    else:
        post = Post()
        post.image = request.POST.get('image',False)
        post.weather = request.POST['weather']
        post.weather_desc = request.POST['weather_desc']
        post.temp = request.POST['temp']
        post.temp_desc = request.POST['temp_desc']
        post.finedust =request.POST.get('finedust')
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
    post_detail = get_object_or_404(Post, id=post_id)
    return render(request, 'detail.html', {'post_detail':post_detail})


def Main(request):
    startdate = date.today()
    enddate = startdate + timedelta(days=1)

    post = Post.objects.filter(created_at__range=[startdate, enddate])

    mypost = post.order_by('-liked')[0]
    print(mypost.weather)

    return render(request, 'Main.html', {"mypost":mypost})

    

def mypage(request,user_id):
    wear_tag = {}
    weather = []
    temp = []
    finedust = []
    temp = 0
    post_num = 0
    user = get_object_or_404(Users, id = user_id)
    post_detail = Post.objects.filter(user = user)
    for post in post_detail:

        weather[int(post.weather)] = weather[int(post.weather)]+1
        finedust[int(post.finedust)] = finedust[int(post.finedust)]+1
        temp = temp + int(post.temp)
        post_num = post_num + 1
        try :
            wear_tag[weather.wear_tag1] = int(wear_tag[weather.wear_tag1]) +1
        except :
            wear_tag[weather.wear_tag1] = 1

    # for post in post_detail :
    #     post
    sorted_dict = sorted(wear_tag.items(), key = lambda item: item[1])
    my_wear = []
    my_wear.append()
    weather = weather.sort(reverse=True)[0]
    finedust = finedust.sort(reverse=True)[0]
    temp_avg = temp/post_num
    my_info = {'weather' : weather, 'finedust' : finedust, 'temp_avg' : temp_avg }


    return render(request,'mypage.html', {'post_detail' : post_detail, 'user_detial' : user, 'my_info' : my_info})
