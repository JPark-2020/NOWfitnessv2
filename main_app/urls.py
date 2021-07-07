from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name="home-page"),
    path('about/', views.About.as_view(), name="about-page"),
    
]
