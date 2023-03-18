from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-id')[:3] #Ordenar y solo mostrar los 3 ultimos
    return render(request, 'home.html', {'posts':posts})

def renderp(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'posts.html', {'posts':posts})

def postdetail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'postd.html', {'post': post})