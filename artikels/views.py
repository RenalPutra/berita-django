from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.hashers import make_password
from .models import *

# Create your views here.

def is_operator(user):
    if user.groups.filter(name="Operator").exists():
        return True
    else:
        return False

@login_required
def dashboard(request):
    template_name = "back/dashboard.html"
    
    if request.user.groups.filter(name="Operator").exists():
        request.session['is_operator'] = 'operator'
    
    mandiri = Informatic.objects.all()
    API_art =  Gamesartikels.objects.all()
    userss = User.objects.all()
    
    context = {
        "mandiri" : mandiri,
        "APIme" : API_art,
        "Usersme" : userss
    }
    
    return render(request, template_name, context)

@login_required
def addartikel(request):
    template_name = "back/add_artikel.html"
    
    if request.method == "POST":
        
        myfile = request.FILES.get("gambar")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)
        
        judul = request.POST.get('judul')
        konten = request.POST.get('konten1')
        gambar = url
        penulis = request.user
        
        Informatic.objects.create(
            penulis = penulis,
            judul = judul,
            konten = konten,
            picture = gambar
        )
        
        return redirect(artikels)
    
    return render(request, template_name)

@login_required
def editartikel(request, id):
    template_name = "back/add_artikel.html"
    
    get_artikel = Informatic.objects.get(id=id)
    
    if request.method == "POST":
        
        myfile = request.FILES.get("gambar")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)
        
        judul = request.POST.get('judul')
        konten = request.POST.get('konten1')
        gambar = url
        penulis = request.user
        
        get_artikel.penulis = penulis
        get_artikel.judul = judul
        get_artikel.konten = konten
        get_artikel.picture = gambar
        get_artikel.save()
        
        
        return redirect(artikels)
    
    context = {
        "value" : get_artikel
    }
    
    return render(request, template_name, context)

@login_required
def deleteartikel(request, id):
    Informatic.objects.get(id=id).delete()
    return redirect(artikels)

@login_required
@user_passes_test(is_operator)
def registerview(request):
    template_name = "account/register.html"
    
    with transaction.atomic():
        if request.method == "POST":
            username = request.POST.get('username')
            get_password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')

            
            User.objects.create(
                username = username,
                password = make_password(get_password),
                first_name = first_name,
                last_name = last_name,
                email = email,
            )
            
            return redirect(dashboard)
    
    return render(request, template_name)

@login_required
def artikels(request):
    
    template_name = "back/artikels.html"
    
    myartikel = Informatic.objects.all()
    
    context= {
        "art" : myartikel
    }
    
    return render(request, template_name, context)