from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login
from .forms import SignupForm ,UserForm,ProfileForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Profile

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = SignupForm()

    return render(request,'registration/signup.html',{'form':form})


@login_required
def profile(request):
        profile = Profile.objects.get(user=request.user)
        return render(request,'accounts/profile.html',{'profile':profile})
        
@login_required
def profile_edit(request):
        profile = Profile.objects.get(user=request.user)
        if request.method == 'POST':
            user_form = UserForm(request.POST,instance=request.user)
            profile_form = ProfileForm(request.POST,instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                myprofile = profile_form.save(commit=False)
                myprofile.user = request.user
                myprofile.email = request.user.email
                myprofile.save()
                return redirect(reverse('accounts:profile'))
        else :
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
            
        return render(request,'accounts/profile_edit.html',{'user_form':user_form,'profile_form':profile_form})
    