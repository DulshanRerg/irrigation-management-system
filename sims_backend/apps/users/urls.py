from django.urls import path
from .views import RegisterView, LoginView, ProfileView, PasswordResetRequestView, PasswordResetConfirmView, ObtainTokenView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password-reset-request/', PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('token/', ObtainTokenView.as_view(), name='token'),
]