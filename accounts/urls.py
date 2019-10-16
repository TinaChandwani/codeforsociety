from django.urls import path

# url for home page
from . import views
urlpatterns=[
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('register',views.register, name='register'),
    path('password-reset/', views.password_reset, name = 'password_reset'),
    path('password-reset/done/', views.password_reset_done, name = 'password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.password_reset_confirm, name ='password_reset_confirm'),
    path('dashboard', views.dashboard, name="dashboard")
]