
from django.urls import path, include, re_path
from . import views
# api versioning

#rutas
urlpatterns = [
    re_path('login', views.login),
    re_path('register', views.register),
    re_path('profile', views.profile),
]

#Todo esto crea las rutas, GET, POST, PUT, DELETE.
