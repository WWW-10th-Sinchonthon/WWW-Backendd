from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Post, Scrap
from .forms import CreateForm

def home(request):
    return render(request, 'Main.html')

def create(request):
    if(request.method == 'POST' or request.method == 'FILES'):
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        post=Post.objects.filter().order_by('-id')[0]
        return redirect('detail', post.id)
    else:
        form = CreateForm()
        return render(request, 'create.html', {'form':form})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post_detail':post_detail})



def mypage(request):
    return render(request, 'mypage.html')