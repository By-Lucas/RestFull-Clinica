from rest_framework import viewsets

from  pacientes.models import Pacientes
from  pacientes.api.serializers import  Pacientes_Serializer

class  Pacientes_viewsets(viewsets.ModelViewSet):
    queryset = Pacientes.objects.all() # pegar todos os registros
    serializer_class =  Pacientes_Serializer # pegar os serializers