# Generated by Django 2.2.7 on 2020-02-04 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operative', '0020_auto_20191202_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/documentos/'),
        ),
    ]
