
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("addartikel/", addartikel, name="addartikel"),
    path("register/", registerview, name="register"),
    path("artikels/", artikels, name="artikels"),
    path("editartikels/<int:id>", editartikel, name="editartikels"),
    path("deleteartikels/<int:id>", deleteartikel, name="deleteartikels"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)