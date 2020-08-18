# Generated by Django 3.0.7 on 2020-08-18 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('cnpj', models.CharField(default='Nome', max_length=250)),
                ('valor', models.FloatField(blank=True, default=0)),
            ],
        ),
    ]
