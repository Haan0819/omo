from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('signin/', views.signin, name='login'),
    path('', views.index, name='index'),
]