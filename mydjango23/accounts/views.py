from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from PIL import Image

login = LoginView.as_view(
    template_name="accounts/login.html",

)


def profile_image(reqeust: HttpRequest) -> HttpResponse:
    canvas = Image.new("RGBA", (256, 256), (255, 0, 0, 255))
    # text / image

    response = HttpResponse(content_type="image/png")
    canvas.save(response, "PNG")

    return response


# 새로운 User 인스턴스를 만드는 것.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else:
        form = UserCreationForm()
    return render(
        request,
        "accounts/signup_form.html",
        {
            "form": form,
        }
    )
    pass


# signup = CreateView.as_view(
#     form_class=UserCreationForm,
#     success_url=reverse_lazy("accounts:login"),
#     template_name="accounts/signup_form.html"
# )

@login_required
def profile(request):
    return render(request, "accounts/profile.html")


logout = LogoutView.as_view(
    next_page="accounts:login",
)
