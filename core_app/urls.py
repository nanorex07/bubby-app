from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm


app_name = "core_app"


urlpatterns: list[str] = [
    path("", views.index, name="index"),
    path("page/<int:page>/", views.index, name="index_page"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("profile/update/", views.update_profile, name="update_profile"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("login/", auth_views.LoginView.as_view(template_name="core_app/login.html",
         authentication_form=LoginForm), name="login"),
]
