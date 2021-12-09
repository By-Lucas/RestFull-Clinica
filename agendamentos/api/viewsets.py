from rest_framework import viewsets

from  agendamentos.models import Agendamentos
from  agendamentos.api.serializers import Agendamentos_serializer

# segue o padrao junto com as bibliotecas importadas

class Agendamentos_viewsets(viewsets.ModelViewSet):
    queryset = Agendamentos.objects.all().order_by('data_hora') # ordenar por data e hora
    serializer_class = Agendamentos_serializer