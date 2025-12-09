from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from empleado.models import Empleado
from usuario.models import Usuario
# Create your views here.

@api_view(['POST'])
def login(request):
    return Response({})


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():

        # 1. Extraer empleado del request
        empleado_id = serializer.validated_data.pop('empleado')

        # 2. Crear User correctamente
        user = User.objects.create_user(
            username=serializer.data['username'],
            email=serializer.data['email'],
            password=serializer.data['password']
        )

        # 3. Buscar empleado usando el nombre REAL del campo
        empleado = Empleado.objects.get(id_empleado=empleado_id)

        # 4. Crear Usuario (perfil)
        usuario = Usuario.objects.create(
            user=user,
            empleado=empleado
        )

        # 5. Crear Token
        token = Token.objects.create(user=user)

        # 6. Respuesta final
        return Response({
            "token": token.key,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "empleado": empleado.id_empleado,
                "usuario_id": usuario.id_usuario
            }
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def profile(request):
    return Response({})