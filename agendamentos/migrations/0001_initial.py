# Generated by Django 3.2.9 on 2021-12-03 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamentos',
            fields=[
                ('id_agendamento', models.AutoField(primary_key=True, serialize=False)),
                ('data_hora', models.DateTimeField(blank=True, null=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('cancelado', models.BooleanField(default=False)),
                ('obs', models.TextField(blank=True, null=True)),
                ('tipo', models.CharField(blank=True, max_length=100, null=True)),
                ('id_pacientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agendamentos', to='pacientes.pacientes')),
            ],
            options={
                'db_table': 'agendamentos',
                'managed': True,
                'unique_together': {('data_hora', 'id_pacientes')},
            },
        ),
    ]
