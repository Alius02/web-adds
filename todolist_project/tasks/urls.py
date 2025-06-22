from django.urls import path
from .views import (
    UserRegistrationAPIView,
    UserProfileAPIView,
    AppInfoAPIView,
    TaskListCreateAPIView,
    TaskRetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Маршрути для користувачів:
    path('users/register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('users/profile/', UserProfileAPIView.as_view(), name='user-profile'),

    # Маршрут для інформації про додаток:
    path('info/', AppInfoAPIView.as_view(), name='app-info'),

    # Маршрути для задач:
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),
]