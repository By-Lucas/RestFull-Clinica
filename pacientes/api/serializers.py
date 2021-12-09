from  rest_framework import serializers

from pacientes.models import Pacientes


class Pacientes_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes # Usar sempre este modelo
        fields = '__all__' # pegar todos os campos da classe pacientes importada