from django.shortcuts import render


# Create your views here.
def create_news(request):
    return render(request, "news/create.html")


def read_news(request):
    return render(request, "news/read.html")


def update_news(request):
    return render(request, "news/update.html")


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