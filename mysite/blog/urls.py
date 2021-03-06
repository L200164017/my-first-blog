
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
