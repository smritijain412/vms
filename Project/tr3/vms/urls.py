from django.urls import path
from . import views
# from django.conf.urls import url

app_name = 'vms'

urlpatterns = [
    path('', views.home, name='home'),

    path('visitor/', views.visitors, name='visitor'),
    path('employee/<int:pk>/', views.employee_dash, name='employee_dash'),
    path('employee/', views.employee, name='employee'),
    path('create_visit/', views.createVisit, name='create_visit'),
    path('update_visit/<int:pk>/', views.updateVisit, name='update_visit'),
    path('delete_visit/<int:pk>/', views.deleteVisit, name='delete_visit'),

    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login, name='login'),
    # path('api/', views.RegisterAPI.as_view(), name='register'),
]
