from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
        path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
]
