from django.urls import path
from .views import UserRegistrationView, TestListView, CabinetView

app_name = 'users'

urlpatterns = [
    path('accounts/register/', UserRegistrationView.as_view(), name='register'),
    path('users/list/', TestListView.as_view(), name='test'),
    path('accounts/cabinet/', CabinetView.as_view(), name='cabinet')
]
