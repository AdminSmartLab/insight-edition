# Generated by Django 2.2.7 on 2021-09-14 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operative', '0004_auto_20210903_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='pdf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documentos', to='files.PDF'),
        ),
    ]
