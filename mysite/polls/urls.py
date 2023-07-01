# file used to map views to urls (URLconf file)
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
