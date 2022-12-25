from django.contrib import admin
from .models import *
# Register your models here.

class Admingame(admin.ModelAdmin):
    list_display = ["title", "thumb", "date", 'desc', 'key']

admin.site.register(Gamesartikels, Admingame)

class AdminInformatics(admin.ModelAdmin):
    list_display = ["penulis","judul", "konten", "date", "picture"]

admin.site.register(Informatic, AdminInformatics)