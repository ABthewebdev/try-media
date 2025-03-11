from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/follow/<int:profile_id>/', views.follow_toggle, name='follow_toggle')
]