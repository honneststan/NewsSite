from django.shortcuts import render, redirect
from .forms import CreateNewsForm, UpdateNewsForm
from .models import News
from .webscrapers import baahrakhari_webscraping
from .webscrapers import ekantipur_webscraping
from .webscrapers import gorkhapatraonline_webscraping
from .webscrapers import onlinekhabar_webscraping


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


def webscrap_news(request):
    baahrakhari_newses = baahrakhari_webscraping.baahrakhari_list_webscraping()
    ekantipur_newses = ekantipur_webscraping.ekantipur_list_webscraping()
    gorkhapatraonline_newses = gorkhapatraonline_webscraping.gorkhapatraonline_list_webscraping()
    onlinekhabar_newses = onlinekhabar_webscraping.onlinekhabar_list_webscraping()
    newses = baahrakhari_newses + ekantipur_newses + gorkhapatraonline_newses + onlinekhabar_newses
    for news in newses:
        registered_news = News.objects.create(title=news[0], image=news[1], source=news[2], description=news[3])
        registered_news.save()
    registered_newses = News.objects.all()
    context ={
        "newses": registered_newses
    }
    return render(request, "news/webscrap.html", context)


