from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('loginpage',views.loginpage),
    path('signup',views.signup),
    path('signin',views.signin),
    path('success',views.success),
    path('logout',views.logout),
    path('wall',views.wall),

]
