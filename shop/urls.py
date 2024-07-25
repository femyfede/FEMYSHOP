from django.urls import path
from . import views

urlpatterns = [
    path('',views.registration, name='regdjango'),
    path('login/',views.login,name='logindjango'),
     path('home/', views.home, name='home'),
]
