from django.urls import path

from accounts.api_endpoints import SessionLoginAPIView, SessionLogoutAPIView
from accounts.api_endpoints import *

urlpatterns = [
    path("login/", SessionLoginAPIView.as_view(), name="login-session"),
    path("logout/", SessionLogoutAPIView.as_view(), name="logout-session"),
]
