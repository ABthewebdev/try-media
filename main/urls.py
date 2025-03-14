from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/follow/<int:profile_id>/', views.follow_toggle, name='follow_toggle'),
    path('<str:username>/<int:post_id>/', views.post, name='post'),
    path('create/', views.create, name='create_post')
]