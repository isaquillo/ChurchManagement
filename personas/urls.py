from django.urls import path
from . import views

urlpatterns = [
    path('personas/listar_personas', views.listar_personas, name='listar_personas')
]
