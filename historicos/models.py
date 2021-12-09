from django.db import models

from  agendamentos.models import Agendamentos

# Create your models here.

class Historicos(models.Model):
    id_historic = models.AutoField(primary_key=True)
    data = models.DateTimeField(auto_now_add=True)
    aparecimentos_sitomas = models.CharField(max_length=100, blank=True, null=True)
    duracao_sitomas = models.CharField(max_length=100, blank=True, null=True)
    local_da_dor = models.CharField(max_length=100, blank=True, null=True)
    local_dor = models.CharField(max_length=100, blank=True, null=True)
    tipo_dor = models.CharField(max_length=100, blank=True, null=True)
    conclusao = models.TextField(blank=True, null=True)
    #Tem vinculo com o Agendamento para que nao tenha historico do mesmo agendamento repetido com mesma data e in cliente
    id_agendamento = models.ForeignKey(Agendamentos, related_name = 'historicos', on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'historicos' #nome da tabela