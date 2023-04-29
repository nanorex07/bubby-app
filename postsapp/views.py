from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import CreatePostForm


def show_post(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)[:10]
    return render(request, "postsapp/view_post.html", {"post": post, "comments": comments})


@login_required
def create_post(request):

    form = CreatePostForm()
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("core_app:index")

    return render(request, "postsapp/create_post.html", {"form": form})


@login_required
def set_like(request, post_id):
    post = Post.objects.get(id=post_id)
    if post:
        if request.user not in post.likes.all():
            post.likes.add(request.user)
        else:
            post.likes.remove(request.user)
        post.save()

    return redirect("postsapp:show_post", post.id)


@login_required
def set_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    if post and request.POST.get("comment"):
        comment = Comment(
            author=request.user,
            content=request.POST["comment"],
            post=post,
        )
        comment.save()

    return redirect("postsapp:show_post", post.id)
