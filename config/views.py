from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, "registration/signup.html", context)

