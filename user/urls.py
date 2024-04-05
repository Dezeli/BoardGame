from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("join/", views.join_page, name="join"),
    path("logout/", views.logout_page, name="logout"),
]
