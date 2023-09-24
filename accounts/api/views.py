from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response

from django.contrib.auth.models import User
from accounts.models import Perfil
from accounts.api.serializers import UserSerializer, UserCreateSerializer, PerfilSerializer

class testeAPIView(APIView):
    '''
    accounts/api/
    Endpoint teste request get. 
    '''

    def get(self, request):
        return Response({"mensagem": "AQUI"})
    

class testeDoisAPIView(APIView):
    '''
    accounts/api/dois/
    Endpoint teste request get. 
    {
        'mensagem': Texto
    }
    URL: ?mensagem=Texto
    '''

    def get(self, request):
        mensagem = request.GET.get("mensagem")
        return Response({"mensagem": mensagem})
    

# generics.GenericAPIView -> Funcionalidade básica serializer, queryset, .as_view()
# ListModelMixin -> Método GET para carregar lista de instâncias
class UserAPIView(generics.ListAPIView):
    '''
    accounts/api/usuarios/
    Endpoint para listar usuários request get. 
    {
        "username__icontains": "ub"
    }
    ?username=ubuntu
    ?username__icontains=ub
    '''

    serializer_class    = UserSerializer
    queryset            = User.objects.all()

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    def get_queryset(self):
        dicionario_request = self.request.GET.dict()
        return self.queryset.filter(**dicionario_request)
    

class UserCreateAPIView(generics.CreateAPIView):
    '''
    accounts/api/usuarios/create/
    Endpoint para criar usuário request post. 
    '''

    serializer_class    = UserCreateSerializer
    queryset            = User.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProfileAPIView(generics.ListCreateAPIView):
    '''
    accounts/api/profiles/
    Endpoint para listar perfils request get e post. 
    '''

    serializer_class    = PerfilSerializer
    queryset            = Perfil.objects.all()

    def get_queryset(self):
        dicionario_request = self.request.GET.dict()
        return self.queryset.filter(**dicionario_request)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class ProfilePKAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''
    accounts/api/profiles/<pk>/
    Endpoint para listar usuários request get. 
    '''

    serializer_class    = PerfilSerializer
    queryset            = Perfil.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)