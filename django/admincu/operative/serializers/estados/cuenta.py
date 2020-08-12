from .base import *
from django.db.models import Sum


class EstadoCuentaModelSerializer(EstadoBaseModelSerializer):
	"""
		Estado de Cuenta
	"""

	saldo = serializers.SerializerMethodField()
	concepto = serializers.SerializerMethodField()

	class Meta:
		model = Operacion

		fields = (
			'saldo',
			'concepto'
		)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields.pop('monto')
		self.fields['cuenta'] = serializers.CharField(max_length=200, required=True)
		self.fields['debe'] = serializers.DecimalField(read_only=True, decimal_places=2, max_digits=15)
		self.fields['haber'] = serializers.DecimalField(read_only=True, decimal_places=2, max_digits=15)
		self.orden = 0
		self.saldo = 0.00


	def get_saldo(self, obj):
		if self.orden == 0:
			self.saldo = Operacion.objects.filter(
				cuenta=obj.cuenta,
				fecha__lte=obj.fecha,
				id__lte=obj.id
			).aggregate(calculo=Sum('valor'))['calculo'] or 0
		else:
			self.saldo = self.saldo + obj.debe() - obj.haber()

		self.orden += 1

		return self.saldo

	def get_concepto(self, obj):
		texto = "" 
		if obj.ingreso():
			texto += obj.ingreso().nombre
		else:
			texto += "SF"
		if obj.vinculo:
			texto += " {}".format(obj.vinculo.periodo()) 	
		else:
			texto += " {}".format(obj.periodo()) 
		return texto