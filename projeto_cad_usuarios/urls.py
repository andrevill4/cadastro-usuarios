from django.contrib import admin
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('usuarios/', views.listagem_usuarios, name='listagem_usuarios'),
    path('excluir_usuario/<int:id>/', views.excluir_usuario, name='excluir_usuario'),

]
 