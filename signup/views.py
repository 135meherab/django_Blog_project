from django.shortcuts import render
from . signup_form import SignUpForm
from django.contrib import messages
from author.models import Author
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Author.objects.create(author=user)
            messages.success(request, 'Successfully created account')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})