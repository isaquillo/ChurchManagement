from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/signup/', views.signup, name='signup'),
    path('login/logout/', views.signout, name='logout'),
    path('login/signin/', views.signin, name='login')
]
