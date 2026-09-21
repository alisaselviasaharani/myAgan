from django.urls import path

from main.views import (
    show_home,
    show_about,
    show_collection,
    create_collection,
)

app_name = "main"

urlpatterns = [
    path("", show_home, name="show_home"),
    path("about/", show_about, name="show_about"),
    path("collection/", show_collection, name="show_collection"),
    path("collection/add/", create_collection, name="create_collection"),
]