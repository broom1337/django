from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('news_list/', views.news, name = 'news'),
    path('news_list/detail/<int:pk>/', views.detail, name = 'post_detail'),
]

app_name = "post"