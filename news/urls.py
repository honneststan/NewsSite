from django.urls import path
from .views import create_news, read_news, update_news, delete_news, view_news
from .views import update_profile, view_profile

from config.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = "news"

urlpatterns = [
    path("news/create", create_news, name="create-news"),
    path("news/read", read_news, name="read-news"),
    path("news/update/<int:pk>", update_news, name="update-news"),
    path("news/delete/<int:pk>", delete_news, name="delete-news"),
    path("news/view/<int:pk>", view_news, name="view-news"),
    path("profile/update", update_profile, name="update-profile"),
    path("profile/view", view_profile, name="view-profile"),

] + static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
