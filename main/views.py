from django.shortcuts import render, redirect
from main.models import About
from main.forms import CollectionForm


def show_home(request):
    context = {
        "website": "Hai aku afgan suami asya selamanya!!",
        "liat": "Kalian Harus liat LAGU INI!!"
    }
    return render(request, "index.html", context)


def show_about(request):
    context = {
        "about_list": About.objects.all()
    }
    return render(request, "about.html", context)


def show_collection(request):
    return render(request, "collection.html")


def create_collection(request):
    form = CollectionForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("main:show_collection")

    context = {
        "form": form
    }

    return render(request, "create.html", context)