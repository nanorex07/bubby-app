from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import SignUpForm, UpdateProfileForm
from .models import Profile

from postsapp.models import Post


def index(request, page=1):
    results_per_page = 5
    start = results_per_page*(page-1)
    posts = Post.objects.all()

    maxPage = len(posts) // 5 + int(len(posts) % 5 > 0)
    return render(request=request, template_name="core_app/index.html", context={
        "posts": posts[start:start+results_per_page], "page": page, "max_page": maxPage
    })


@user_passes_test(lambda user: not user.is_authenticated)
def signup(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.POST.get("username"))
            profile = Profile.objects.create(user=user)
            profile.save()
            return redirect("core_app:login")

    else:
        form = SignUpForm()
    return render(request, "core_app/signup.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("core_app:index")


@login_required
def profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, "core_app/profile.html", {"user": user})


@login_required
def update_profile(request):
    if request.method == "POST":
        form = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("core_app:profile", user_id=request.user.id)
        else:
            return render(request, "core_app/update_profile.html", {"form": form})

    form = UpdateProfileForm(instance=request.user.profile)
    return render(request, "core_app/update_profile.html", {"form": form})
