from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('detail/<int:video_id>', views.detail, name='detail'),
    path('edit/<int:video_id>', views.edit, name='edit'),
    path('delete/<int:video_id>', views.delete, name='delete'),
    path('signin/', views.signin, name='signin'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]