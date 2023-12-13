from django.shortcuts import render, redirect
from . form import BlogForm
from django import forms
from . models import Blog
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login_page')
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user.author
            form.save()
            return redirect('home_page')
    else:
        form = BlogForm()
    return render (request, 'add_blog.html', {'form': form})