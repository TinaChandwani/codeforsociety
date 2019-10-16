from django.urls import path

# url for home page
from . import views
urlpatterns=[
    path('',views.workshops, name='workshops'),
    path('<int:workshop_id>',views.workshop, name='workshop'),
    path('search', views.search, name="search")
]