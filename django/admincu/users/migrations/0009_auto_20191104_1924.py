# Generated by Django 2.2.6 on 2019-11-04 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20191027_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='nombre',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
