# Generated by Django 2.2 on 2019-05-15 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operative', '0002_auto_20190510_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='nombre',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='numero',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
