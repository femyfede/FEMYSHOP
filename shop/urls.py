from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('',views.registration, name='regdjango'),
    path('logindjango/',views.login,name='logindjango'),
     path('home/', views.home, name='home'),
]
