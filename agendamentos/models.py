from django.db import models

from  pacientes.models import Pacientes
# Create your models here.

class  Agendamentos(models.Model):
    id_agendamento = models.AutoField(primary_key=True)
    data_hora = models.DateTimeField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add = True)
    cancelado = models.BooleanField(default=False)
    obs = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    # abaixo ele vincula com a outra tabela pacientes e ver se tem clientes com mesmo id e nome agendado para o mesmo horario
    # e relata a informacao / resumindo isso nao pode
    id_pacientes = models.ForeignKey(Pacientes, on_delete=models.CASCADE, related_name='agendamentos', blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'agendamentos' # Nome da tabela vai ser agendamentos
        unique_together = ('data_hora', 'id_pacientes') # nao pode haver agendamentos da mesma pessoa para o mesmo horario
