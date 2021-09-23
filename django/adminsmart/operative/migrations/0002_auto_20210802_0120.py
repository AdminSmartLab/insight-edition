# Generated by Django 2.2.7 on 2021-08-02 01:20

from django.db import migrations, models
import django.db.models.deletion
import django_afip.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operative', '0001_initial'),
        ('afip', '0004_storages_and_help_texts'),
        ('utils', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='titulo',
            name='comunidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.Comunidad'),
        ),
        migrations.AddField(
            model_name='titulo',
            name='predeterminado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titulos', to='operative.Naturaleza'),
        ),
        migrations.AddField(
            model_name='titulo',
            name='supertitulo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subtitulos', to='operative.Titulo'),
        ),
        migrations.AddField(
            model_name='taxon',
            name='naturaleza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='taxones', to='operative.Naturaleza'),
        ),
        migrations.AddField(
            model_name='ownreceipt',
            name='concept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='own_receipts', to='afip.ConceptType', verbose_name='concept'),
        ),
        migrations.AddField(
            model_name='ownreceipt',
            name='currency',
            field=models.ForeignKey(blank=True, default=django_afip.models.first_currency, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='own_receipts', to='afip.CurrencyType', verbose_name='currency'),
        ),
        migrations.AddField(
            model_name='ownreceipt',
            name='document_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='own_receipts', to='afip.DocumentType', verbose_name='document type'),
        ),
        migrations.AddField(
            model_name='ownreceipt',
            name='receipt_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='own_receipts', to='afip.ReceiptType', verbose_name='receipt type'),
        ),
        migrations.AddField(
            model_name='operacion',
            name='comunidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.Comunidad'),
        ),
        migrations.AddField(
            model_name='operacion',
            name='cuenta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='operaciones', to='operative.Cuenta'),
        ),
        migrations.AddField(
            model_name='operacion',
            name='documento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='operaciones', to='operative.Documento'),
        ),
        migrations.AddField(
            model_name='operacion',
            name='metodos',
            field=models.ManyToManyField(blank=True, to='operative.Metodo'),
        ),
        migrations.AddField(
            model_name='operacion',
            name='vinculo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vinculos', to='operative.Operacion'),
        ),
        migrations.AddField(
            model_name='metodo',
            name='comunidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.Comunidad'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='comunidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.Comunidad'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='grupo_siguiente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grupo_anterior', to='operative.Grupo'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='metodos',
            field=models.ManyToManyField(blank=True, to='operative.Metodo'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='taxon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='operative.Taxon'),
        ),
        migrations.AddField(
            model_name='documento',
            name='comunidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.Comunidad'),
        ),
        migrations.AddField(
            model_name='documento',
            name='destinatario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documentos', to='operative.Cuenta'),
        ),
        migrations.AddField(
            model_name='documento',
            name='receipt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='documentos', to='operative.OwnReceipt'),
        ),
        migrations.AddField(
            model_name='documento',
            name='receipt_afip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='documentos', to='afip.Receipt'),
        ),
        migrations.AddField(
            model_name='definicionvinculo',
            name='cuenta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vinculo1', to='operative.Cuenta'),
        ),
        migrations.AddField(
            model_name='definicionvinculo',
            name='cuenta_vinculada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vinculo2', to='operative.Cuenta'),
        ),
        migrations.AddField(
            model_name='definicionvinculo',
            name='definicion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='operative.Taxon'),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='comunidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.Comunidad'),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='domicilio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='utils.Domicilio'),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='grupos',
            field=models.ManyToManyField(blank=True, to='operative.Grupo'),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='metodos',
            field=models.ManyToManyField(blank=True, to='operative.Metodo'),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='naturaleza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='operative.Naturaleza'),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='perfil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Perfil'),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='taxon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='operative.Taxon'),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='titulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='operative.Titulo'),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='vinculos',
            field=models.ManyToManyField(blank=True, through='operative.DefinicionVinculo', to='operative.Cuenta'),
        ),
    ]
