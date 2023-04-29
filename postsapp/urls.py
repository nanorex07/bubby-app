from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "postsapp"


urlpatterns: list[str] = [
    path("create/", views.create_post, name="create_post"),
    path("<post_id>/", views.show_post, name="show_post"),
    path("<post_id>/like/", views.set_like, name="set_like"),
    path("<post_id>/comment/", views.set_comment, name="comment")
]
