from django.db import models

# Create your models here.

class Pacientes(models.Model):
    id_paciente = models.AutoField(primary_key=True)# Implementar ID automaticamente
    nome = models.CharField(max_length=100, blank=True, null=True) # Nao precisa ser obrigatorio
    data_nascimento = models.DateTimeField(blank=True, null=True)
    endereco = models.CharField(max_length=80, blank=True, null=True)
    numero_endereco = models.IntegerField(blank=True, null=True)
    bairro_endereco = models.CharField(max_length=60, blank=True, null=True)
    cep = models.CharField(max_length=50, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    rg = models.CharField(max_length=50, blank=True, null=True)

    class  Meta:
        managed = True
        db_table = 'pacientes' #criar tabela e o nome ser pacientes