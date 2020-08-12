# from .individual import *
# from .masivo import *
from django.db import transaction

from admincu.operative.models import Operacion
from admincu.operative.serializers.operaciones.cliente import CreditoModelSerializer


class PreConceptoModelSerializer(CreditoModelSerializer):
	'''Operacion de saldo a favor de cliente, solo lectura'''

	def get_metodo(self, cuenta, naturaleza):
		
		try:
			return cuenta.metodos.get(naturaleza=naturaleza)
		except:
			return

	@transaction.atomic
	def create(self, validated_data):
		operaciones = []
		metodo_interes = self.get_metodo(cuenta=validated_data['ingreso'], naturaleza='interes')
		metodo_descuento = self.get_metodo(cuenta=validated_data['ingreso'], naturaleza='descuento') 
		operacion_debe = Operacion.objects.create(
			comunidad=self.context['comunidad'],
			cuenta=validated_data['destinatario'],
			valor=validated_data['monto'],
			detalle=validated_data['detalle'],
			fecha_indicativa=validated_data['periodo'],
			fecha_gracia=validated_data['fecha_gracia'],
			fecha_vencimiento=validated_data['fecha_vencimiento'],
		)
		if metodo_interes:
			operacion_debe.metodos.add(metodo_interes)
		if metodo_descuento:
			operacion_debe.metodos.add(metodo_descuento)
		
		operaciones.append(operacion_debe)
		operacion_haber = Operacion.objects.create(
			comunidad=self.context['comunidad'],
			cuenta=validated_data['ingreso'],
			valor=-validated_data['monto'],
			detalle=validated_data['detalle'],
			vinculo=operacion_debe,
			fecha_indicativa=validated_data['periodo'],
			)
		operaciones.append(operacion_haber)

		return operaciones

	@transaction.atomic
	def update(self, instance, validated_data):
		"""
			Se actualiza: Cuenta, Perfil y Domicilio.
			Se construye un cliente completo.
		"""
			
		# Actualizacion de Nombre
		instance.cuenta = validated_data['destinatario']
		instance.valor = validated_data['monto']
		instance.detalle = validated_data['detalle']
		instance.fecha_indicativa = validated_data['periodo']
		instance.fecha_gracia = validated_data['fecha_gracia']
		instance.fecha_vencimiento = validated_data['fecha_vencimiento']
		instance.save()

		instance_ingreso = instance.vinculos.filter(cuenta__naturaleza__nombre="ingreso").first()
		instance_ingreso.cuenta = validated_data['ingreso']
		instance_ingreso.valor = -validated_data['monto']
		instance_ingreso.detalle = validated_data['detalle']
		instance_ingreso.fecha_indicativa = validated_data['periodo']
		instance_ingreso.save()

		return instance		