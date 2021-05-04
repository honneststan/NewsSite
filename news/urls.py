from django.urls import path
from .views import create_news, read_news, update_news, delete_news, view_news, search_news
from .views import update_profile, view_profile

app_name = "news"

urlpatterns = [
    path("news/create", create_news, name="create-news"),
    path("news/read", read_news, name="read-news"),
    path("news/update", update_news, name="update-news"),
    path("news/delete", delete_news, name="delete-news"),
    path("news/view", view_news, name="view-news"),
    path("news/search", search_news, name="search-news"),
    path("profile/update", update_profile, name="update-profile"),
    path("profile/view", view_profile, name="view-profile"),

]
