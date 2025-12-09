from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    empleado = serializers.IntegerField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'empleado']
