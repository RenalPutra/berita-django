from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Gamesartikels(models.Model):
    title = models.CharField(max_length=225)
    thumb = models.CharField(max_length=225)
    date = models.CharField(max_length=225)
    desc = models.TextField()
    key = models.CharField(max_length=225)
    
class Informatic(models.Model):
    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    judul = models.CharField(max_length=200) 
    konten = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    picture = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return "{} - {}".format(self.judul, self.konten)
    

