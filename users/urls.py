from django.urls import path
from .views import *

urlpatterns =[
    path("login/", auth, name="login"),
    path("sighup/", register, name="register"),
    path("logout/",loggout_view, name="logout")
]