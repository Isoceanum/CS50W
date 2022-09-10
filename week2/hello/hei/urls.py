from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("petter", views.petter, name="petter"),
    path("<str:name>", views.hils, name="hils")
]