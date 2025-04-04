from django.urls import path
from .views import get_user_visits

urlpatterns = [
    path('user-visits/', get_user_visits, name='user_visits'),
]