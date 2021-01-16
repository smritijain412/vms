from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'admin_user'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('api/', views.RegisterAPI.as_view(), name='register'),
]
