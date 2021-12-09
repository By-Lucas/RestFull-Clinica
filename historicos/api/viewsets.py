from rest_framework import viewsets

from historicos.api.serializres import  Historicos_serializer
from historicos.models import Historicos

# segue padrao dos outros junto com as bibliotecas importadas
class  Historicos_viresets(viewsets.ModelViewSet):
    queryset = Historicos.objects.all().order_by('data')
    serializer_class = Historicos_serializer