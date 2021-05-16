from django.shortcuts import render, redirect
from .forms import CreateNewsForm, UpdateNewsForm
from .models import News


# Create your views here.
def create_news(request):
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




def read_news(request):
    return render(request, "news/read.html")


def update_news(request, pk):
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

def delete_news(request):
    return render(request, "news/delete.html")


def view_news(request):
    return render(request, "news/view.html")


def search_news(request):
    return render(request, "news/search.html")


def update_profile(request):
    return render(request, "profile/update.html")


def view_profile(request):
    return render(request, "profile/view.html")