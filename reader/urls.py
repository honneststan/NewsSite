from django.urls import path, include

from config.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "reader"

urlpatterns = [



] + static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()