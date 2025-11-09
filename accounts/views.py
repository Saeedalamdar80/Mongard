from django.shortcuts import redirect, render
from .forms import UserLoginForm, UserRegistrationForm 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def user_register(request):
    if request.method == 'POST': # user submmited form informations
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'user registered successflly', 'success')
            user.first_name = cd['first_name']
            user.last_name = cd["last_name"]
            user.save()
            return redirect('home')
    else:
        form = UserRegistrationForm() # GET mehton -> comes with url into this page and i have to show the form
    return render(request, 'register.html', {'form':form}) 
      
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password = cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'logged in successfully', 'success')
                return redirect('home')
            else:
                messages.error(request, 'username or password is wrong', 'danger')

    else:
        form = UserLoginForm()
    return render(request, 'login.html', {"form": form})

def user_logout(request):
    logout(request)
    messages.success(request, 'logged out successfully', 'success')
    return redirect('home')