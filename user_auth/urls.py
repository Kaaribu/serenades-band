from django.urls import path
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.login_request, name='user_auth'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('register/', views.register, name='register'),
]