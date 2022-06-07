from django.urls import path 
from . import views


urlpatterns = [
    path('', views.login_page, name='login'), 
    path('register/', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile, name='profile'),
    # path('', views.gallery, name='gallery'),
    
   

]