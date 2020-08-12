from django.db import transaction

from .base import *

from admincu.operative.models import (
	Operacion,
)

from admincu.operative.CU.operaciones.clientes import masivo as operacionesMasivo


class DistribucionSerializer(serializers.Serializer):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['ingreso'] = serializers.PrimaryKeyRelatedField(
				queryset=Cuenta.objects.filter(
						comunidad=self.context['comunidad'], 
						naturaleza__nombre="ingreso"
					), 
				allow_null=False
			)
		unidades_choices = {
			'socio': "Total por socio",
			'dominio': "Total por dominio",	
			'm2': "Total por m2",
		}
		self.fields['unidad'] = serializers.ChoiceField(choices=unidades_choices)
		self.fields['fecha_gracia'] = serializers.DateField(allow_null=True)
		self.fields['fecha_vencimiento'] = serializers.DateField(allow_null=True)
		self.fields['monto'] = serializers.DecimalField(decimal_places=2, max_digits=15, min_value=0.01)


class MasivoClienteModelSerializer(DocumentoModelSerializer):
	'''Documento con destino a cliente model serializer'''

		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['distribuciones'] = DistribucionSerializer(read_only=False, many=True, context=self.context)

		self.fields['preconceptos'] = serializers.PrimaryKeyRelatedField(
				queryset=Operacion.objects.filter(
					comunidad=self.context['comunidad'], 
					documento__isnull=True,
					fecha__isnull=True,
					cuenta__naturaleza__nombre__in=["cliente", "dominio"],
				), many=True
			)
		

	@transaction.atomic
	def create(self, validated_data):
		documento = Documento(
			comunidad=self.context['comunidad'],
			fecha_operacion=fecha_operacion,
		)					
		operacionesMasivo.CU(documento, validated_data).create()
		return 