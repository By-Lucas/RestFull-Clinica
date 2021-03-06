# Generated by Django 3.2.9 on 2021-12-03 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agendamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historicos',
            fields=[
                ('id_historic', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('aparecimentos_sitomas', models.CharField(blank=True, max_length=100, null=True)),
                ('duracao_sitomas', models.CharField(blank=True, max_length=100, null=True)),
                ('local_da_dor', models.CharField(blank=True, max_length=100, null=True)),
                ('local_dor', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_dor', models.CharField(blank=True, max_length=100, null=True)),
                ('conclusao', models.TextField(blank=True, null=True)),
                ('id_agendamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historicos', to='agendamentos.agendamentos')),
            ],
            options={
                'db_table': 'historicos',
                'managed': True,
            },
        ),
    ]
