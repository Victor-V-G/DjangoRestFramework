
from django.urls import path, include
from rest_framework import routers
from usuario import views
from rest_framework.documentation import include_docs_urls

# api versioning
router = routers.DefaultRouter()
router.register(r'usuario', views.UsuarioView, 'usuario')

#rutas
urlpatterns = [
    path("api/v1/", include(router.urls)),

    #documentacion automatica, alojada en http://127.0.0.1:8000/usuario/docs/
    path('docs/', include_docs_urls(title="Usuario API"))
]

#Todo esto crea las rutas, GET, POST, PUT, DELETE.
