from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('signin/', views.signin, name='signin'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]