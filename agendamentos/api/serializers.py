from rest_framework import serializers

from  agendamentos.models import Agendamentos

# esse segue um padrao simples

class  Agendamentos_serializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamentos
        fields = '__all__'