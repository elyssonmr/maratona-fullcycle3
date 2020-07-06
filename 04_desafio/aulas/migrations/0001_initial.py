# Generated by Django 3.0.8 on 2020-07-06 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Aula')),
                ('data_lancamento', models.DateField(verbose_name='Data Lançamento')),
                ('disponivel', models.BooleanField(default=True, verbose_name='Disponivel?')),
            ],
        ),
    ]
