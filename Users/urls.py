from django.urls import path, include
from .views import RegisterView, LoginView, LogoutView, ProfileView
from django.http import JsonResponse


def home_view(request):
    return JsonResponse({"message": "Welcome to Onyinyechi API!"})


urlpatterns = [
    path("", home_view, name="home"),
    path("api/users/register/", RegisterView.as_view(), name="register"),
    path("api/users/login/", LoginView.as_view(), name="login"),
    path("api/users/logout/", LogoutView.as_view(), name="logout"),
    path("api/users/profile/", ProfileView.as_view(), name="profile"),
]