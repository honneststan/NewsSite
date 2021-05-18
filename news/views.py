from django.shortcuts import render, redirect
from .forms import CreateNewsForm, UpdateNewsForm, UpdateProfileForm
from .models import News
from reader.models import Reader


# Create your views here.
def create_news(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CreateNewsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('news:read-news')
        else:
            form = CreateNewsForm()
        context = {
            'form': form
        }
        return render(request, "news/create.html", context)
    else:
        return redirect("news:read-news")


def read_news(request):
    newses = News.objects.all()
    context = {
        "newses": newses
    }
    return render(request, "news/read.html", context)


def update_news(request, pk):
    if request.user.is_superuser:
        required_news = News.objects.get(id=pk)
        if request.method == 'POST':
            form = UpdateNewsForm(instance=required_news,data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                return redirect('news:read-news')
        else:
            form = UpdateNewsForm(instance=required_news)
        context = {
            'form': form
        }
        return render(request, "news/update.html", context)
    else:
        return redirect("news:read-news")


def delete_news(request, pk):
    if request.user.is_superuser:
        required_news = News.objects.get(id=pk)
        if request.method == "POST":
            required_news.delete()
            return redirect('news:read-news')
        return render(request, "news/delete.html")
    else:
        return redirect("news:read-news")


def view_news(request, pk):
    required_news = News.objects.get(id=pk)
    context = {
        "news": required_news
    }
    return render(request, "news/view.html", context)


def update_profile(request):
    required_reader = Reader.objects.get(id=request.user.id)
    if request.method == "POST":
        form = UpdateProfileForm(instance=required_reader, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news:view-profile')
    else:
        form = UpdateProfileForm(instance=required_reader)
    context = {
        'form': form
    }
    return render(request, "profile/update.html", context)


def view_profile(request):
    required_reader = Reader.objects.get(id=request.user.id)
    context = {
        'reader': required_reader
    }
    return render(request, "profile/view.html", context)