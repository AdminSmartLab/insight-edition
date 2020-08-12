# Generated by Django 2.2.6 on 2019-11-04 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operative', '0016_auto_20191027_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operacion',
            name='vinculos',
        ),
        migrations.AddField(
            model_name='operacion',
            name='vinculo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vinculos', to='operative.Operacion'),
        ),
    ]
