from rest_framework import generics

from receitas.models import Medicamento, Receita
from receitas.api.serializers import MedicamentoSerializer, ReceitaSerializer, ReceitaCUDSerializer


class MedicamentosAPIView(generics.ListCreateAPIView):
    '''
    receita/api/medicamentos/
    Endpoint para listar e criar medicamentos, get e post. 
    '''

    serializer_class    = MedicamentoSerializer
    queryset            = Medicamento.objects.all()

    def get_queryset(self):
        dicionario_request = self.request.GET.dict()
        return self.queryset.filter(**dicionario_request)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class MedicamentosPKAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''
    receita/api/medicamentos/<pk>/
    Endpoint para carregar, atualizar e apagar uma medicamentos. 
    '''

    serializer_class    = MedicamentoSerializer
    queryset            = Medicamento.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class ReceitasCreateAPIView(generics.CreateAPIView):
    '''
    receita/api/
    Endpoint para criar receitas, get e post. 
    '''

    serializer_class    = ReceitaCUDSerializer
    queryset            = Receita.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class ReceitasAPIView(generics.ListAPIView):
    '''
    receita/api/
    Endpoint para listar receitas, get e post. 
    '''

    serializer_class    = ReceitaSerializer
    queryset            = Receita.objects.all()

    def get_queryset(self):
        dicionario_request = self.request.GET.dict()
        return self.queryset.filter(**dicionario_request)
    

class ReceitasPKAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''
    receita/api/<pk>/
    Endpoint para carregar, atualizar e apagar uma receita. 
    '''

    serializer_class    = ReceitaCUDSerializer
    queryset            = Receita.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)