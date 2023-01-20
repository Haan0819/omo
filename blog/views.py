from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login


# Create your views here.


def index(request):
    if request.method == "POST":
        temp = request.POST['num']
        posts = Post()
        posts.about = temp
        posts.save()

        return render(
            request,
            'blog/index.html',
            {
                'temp':posts,
            }
        )

    if request.method == "GET":
        posts = Post.objects.all()
        redirect('blog:index')

        return render(
            request,
            'blog/index.html',
            {
                "posts": posts
            }
        )




def signin(request):
    if request.method == "GET":
        return render(request, 'blog/index.html')

    elif request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog:index')
            else:
                return render(request, 'blog/index.html')



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('blog:index')



