from django.urls import path

# url for home page
from . import views
urlpatterns=[
    path('',views.index, name='index'),
    path('about',views.about, name='about')
]