from  rest_framework import serializers

from historicos.models import Historicos

class  Historicos_serializer(serializers.ModelSerializer):
    class Meta:
        model = Historicos
        fields = '__all__'