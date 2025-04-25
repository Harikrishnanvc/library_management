from django.urls import path

from accounts.views import UserRegisterView, LoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('login/', LoginView.as_view(), name='user_login'),
]
