from django.contrib.auth.views import LoginView
from django.urls import path

from accounts.views import SubmittableLoginView, SubmittablePasswordchangeView, SuccessMessageLogoutView

app_name = 'accounts'
urlpatterns = [
    path("login/", SubmittableLoginView.as_view(), name="login"),
    path("logout/", SuccessMessageLogoutView.as_view(), name="logout"),
    path("password-change/", SubmittablePasswordchangeView.as_view(), name="password_change"),
  ]