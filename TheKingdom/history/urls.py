from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('era/<slug:era>/', views.state_detail, name='state_detail'),
]