
from django.urls import path
from . import views
urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('profile', views.PofileView.as_view(), name='profile'),
    path('logout', views.PofileView.as_view(), name='logout'),
    path('register/', views.UserRegistrationView.as_view(), name='register')
]
