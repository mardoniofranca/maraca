# Generated by Django 3.0.7 on 2020-08-18 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_fornecedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalcompra',
            name='valor',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
