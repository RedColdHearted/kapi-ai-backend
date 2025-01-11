from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
from django.urls import path

app_name = "users"

urlpatterns = [
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
    path(
        "login/",
        LoginView.as_view(
            template_name="users/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
]
