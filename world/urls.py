from django.urls import path
from . import views


app_name = "world"

urlpatterns = [
    path("", views.index, name="index"),
]
