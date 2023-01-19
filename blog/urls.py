from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('chart/', views.my_view, name='chart'),
    path('', views.index, name='index'),
]