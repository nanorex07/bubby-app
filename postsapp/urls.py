from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "postsapp"


urlpatterns: list[str] = [
    path("create/", views.create_post, name="create_post"),
    path("delete_comment/<comment_id>",
         views.delete_comment, name="delete_comment"),
    path("<post_id>/", views.show_post, name="show_post"),
    path("<post_id>/like/", views.set_like, name="set_like"),
    path("<post_id>/comment/", views.set_comment, name="comment"),
    path("<post_id>/delete/", views.delete_post, name="delete_post"),
    path("<post_id>/edit/", views.edit_post, name="edit_post"),
]
