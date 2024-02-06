from django.urls import path, include
from .views import UserRegistrationView,UserVerifyCodeView

app_name="accounts"

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="user_register"),
    path('verify/', UserVerifyCodeView.as_view(), name="user_verify_code"),
]