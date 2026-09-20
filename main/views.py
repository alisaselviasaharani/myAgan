from django.shortcuts import render
from main.models import About
# Create your views here.

def show_home(request):
    context={
        "website": "Hai aku afgan suami asya selamanya!!",
        "liat":"Kalian Harus liat LAGU INI!!"
    }
    return render(request,"index.html",context)

def show_about(request):

    context={
        "about_list":About.objects.all()
    }
    return render(request, "about.html",context)

def show_collection(request):
    return render(request, "collection.html")
