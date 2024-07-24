from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('',views.regstration, name='regdjango'),
    path('login/',views.login,name='logindjango'),
     path('home/', home, name='home'),
]
