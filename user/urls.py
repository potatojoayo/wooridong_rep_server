from django.urls import path
from .views import register_view, check_identification_duplicate_view, get_user_view, LogoutView, delete_user_view, \
    check_phone_number_view, change_password_view
from rest_framework_simplejwt.views import TokenRefreshView

from .views.get_token_view import GetTokenView

urlpatterns = [
    path('token/', GetTokenView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('check-identification-duplicate/', check_identification_duplicate_view, name='check_identification_duplicate'),
    path('check-phone-number/', check_phone_number_view, name='check_phone_number_view'),
    path('get-user/', get_user_view, name='get_user'),
    path('withdraw/', delete_user_view, name='delete_user'),
    path('change-password/', change_password_view, name='change_password_view')
]
