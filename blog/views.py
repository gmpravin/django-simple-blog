from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Blog
# Create your views here.

from .forms import PostForm


def index(request):
    return render(request, 'index.html')


def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            post = form.cleaned_data['content']
            newPost = Blog(title=title, author=author,post=post)
            newPost.save()
            return redirect(to='/blog/posts')

    else:
        form = PostForm()
        return render(request,'post.html',{'form':form})

def posts(request):
    posts=Blog.objects.all()
    return render(request,'posts.html',{'posts':posts})


def showpost(request,id):
    post= Blog.objects.get(id=id)
    return render(request, 'posts.html', {'post': post})


def delete(request,id):
    getId = Blog.objects.filter(id=id).delete()
    return redirect(to='/blog/posts')
