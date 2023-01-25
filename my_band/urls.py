from django.urls import path, include
from django.views.static import serve
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('discography/', views.discography, name='discography'),
    path('tours/', views.tours, name='tours'),
    path('contact/', views.contact_form, name='contact'),
    path('register/', views.register, name='register'),
    path('user_auth/', include("django.contrib.auth.urls")),
    path('user_auth/', include("user_auth.urls")),
]