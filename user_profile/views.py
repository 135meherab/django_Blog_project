from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from add_blog.models import Blog

class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']



# Create your views here.
@login_required(login_url='login_page')
def profile(request):
    data = Blog.objects.filter(author = request.user.author)
    return render(request, 'profile.html',{'data':data})



@login_required(login_url='login_page')
def change_data(request):
    if request.method == 'POST':
        form = ChangeUserData(request.POST, instance=request.user )
        if form.is_valid():
            form.save()
            messages.success(request,'Updated successfully')
    else:
        form = ChangeUserData(instance=request.user)
    return render(request, 'change_user_data.html',{'form':form})


@login_required(login_url='login_page')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password changed successfully')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})