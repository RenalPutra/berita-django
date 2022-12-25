from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from berita.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage, name="homepage"),
    path('hotnews/',hotnews, name="hotnews"),
    path('contact/',contact, name="contact"),
    path('author/',author, name="author"),
    path("sinkron_games/", sinkron_game, name="sinkrongame"),
    path("page/<path:key>",detail_page, name="detail"),
    path('about/',about, name="about"),
    path("login/", loginview, name="login"),
    path("logout/", logout_view, name="logout"),
    path("tech/", tech, name="tech"),
    path("techdetail/<int:id>", detailTech, name="techdetail"),
    # apps
    path("dashboard/", include("artikels.urls"))
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
