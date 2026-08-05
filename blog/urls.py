from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:id>/', views.detail, name='detail'),
    path('create/', views.create_blog, name='create_blog'),
    path('edit/<int:id>/', views.edit_blog, name='edit_blog'),
     path('delete/<int:id>/', views.delete_blog, name='delete_blog'),
]