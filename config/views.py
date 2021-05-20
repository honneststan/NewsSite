from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateProfileForm


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        profile_form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('news:read-news')
    else:
        form = UserCreationForm()
        profile_form = CreateProfileForm()
    context = {
        'form': form,
        'profile_form': profile_form
    }
    return render(request, "registration/signup.html", context)

