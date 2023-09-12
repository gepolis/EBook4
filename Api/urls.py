from django.urls import path
from . import views


urlpatterns = [
    path(r'events/', views.EventsViewSet.as_view()),
    path(r'users/', views.UsersViewSet.as_view()),
    path(r'profile/', views.ProfileViewSet.as_view()),
    path(r'profile/<int:pk>/', views.ProfileViewSet.as_view()),
]