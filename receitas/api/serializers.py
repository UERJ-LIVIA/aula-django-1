from rest_framework import serializers

from django.contrib.auth.models import User

from accounts.models import Perfil
from receitas.models import Medicamento, Receita

from accounts.api.serializers import UserSerializer

class MedicamentoSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    unidade_texto = serializers.SerializerMethodField()

    class Meta:
        model = Medicamento
        fields = ['id', 'date', 'nome', 'dose', 'unidade', 'unidade_texto']
        extra_kwargs = {
            'pub_date': {'read_only': True}, 
        }

    def get_date(self, obj): # get_nome_atributo -> serializers.SerializerMethodField()
        return obj.pub_date.strftime('%d/%m/%Y')
    
    def get_unidade_texto(self, obj):
        return obj.get_unidade_display()
    
    # Manipular variável antes de salvar
    def to_internal_value(self, data):
        data["nome"] = data["nome"].upper()
        return super().to_internal_value(data)
    
    # Validar um dado antes de salvar
    def validate(self, data):
        if data["dose"] <= 0:
            raise serializers.ValidationError("A dose precisa ser acima de 0")
        return data
    

class ReceitaCUDSerializer(serializers.ModelSerializer):
    '''
    CREATE UPDATE DELETE
    '''

    class Meta:
        model = Receita
        fields = '__all__'
        extra_kwargs = {
            'pub_date': {'read_only': True}, 
        }

    # Validar um dado antes de salvar
    def validate(self, data):
        medico = data['medico']
        paciente = data['paciente']
        categoria_medico = medico.perfil.categoria
        if categoria_medico != "MEDICO":
            raise serializers.ValidationError("Este usuário não é um médico.")
        if medico == paciente:
            raise serializers.ValidationError("Um médico não pode receitar para si mesmo.")
        return data


class ReceitaSerializer(serializers.ModelSerializer):
    medico = UserSerializer(read_only=True)
    paciente = UserSerializer(read_only=True)
    medicamento = MedicamentoSerializer(many=True, read_only=True)

    class Meta:
        model = Receita
        fields = '__all__'
        extra_kwargs = {
            'pub_date': {'read_only': True}, 
        }