from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path('login/', views.login, name="login"),
    path('profile/', views.profile, name="profile"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
]