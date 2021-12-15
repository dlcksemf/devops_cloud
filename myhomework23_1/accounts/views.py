from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def login(request):
    pass


def profile(request):
    pass


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("blog:post_list")
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup_form.html", {
        "form": form
    })


def logout(request):
    pass
