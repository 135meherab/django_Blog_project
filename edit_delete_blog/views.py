from django.shortcuts import render, redirect
from add_blog.form import BlogForm
from add_blog.models import Blog
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login_page')
def edit(request, id):
    post = Blog.objects.get(pk=id)
    form = BlogForm(request.POST, instance=post)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            return redirect('profile_page')
    else:
        form = BlogForm(instance=post)

    return render(request, 'edit.html', {'form': form})

@login_required(login_url='login_page')
def delete(request, id):
    post = Blog.objects.get(pk=id)
    post.delete()
    return redirect('profile_page')

