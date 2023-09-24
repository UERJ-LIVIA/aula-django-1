from rest_framework import serializers

from django.contrib.auth.models import User
from accounts.models import Perfil


class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password2']

    # Operações a serem feitas antes de salvar
    def save(self):
        user = User()
        user.email = self.validated_data["email"]
        user.username = self.validated_data["username"]
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({'error': 'As senhas precisam ser iguais.'})
        user.set_password(password)
        user.save()
        return user


class PerfilSerializer(serializers.ModelSerializer):

    class Meta:
        model = Perfil
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'perfil']
