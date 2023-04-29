from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import CreatePostForm, UpdatePostForm


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


@login_required
def delete_post(request, post_id):

    post = Post.objects.get(id=post_id)

    if request.user != post.user:
        return redirect("postsapp:show_post", post.id)

    post.delete()
    return redirect("core_app:index")


@login_required
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user != comment.author:
        return redirect("core_app:index")
    comment.delete()
    return redirect(request.META.get("HTTP_REFERER"))


@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.user != request.user:
        return redirect(request.META.get("HTTP_REFERER"))

    if request.method == "POST":
        form = UpdatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("postsapp:show_post", post.id)

        else:
            return render(request, "postsapp/create_post.html", {"form": form})

    form = UpdatePostForm(instance=post)
    return render(request, "postsapp/create_post.html", {"form": form})
