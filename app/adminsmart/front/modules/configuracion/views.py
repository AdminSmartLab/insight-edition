from adminsmart.apps.core.models import (
	Cuenta,
	Metodo,
	Titulo
)

from ..base import AdminModuleView

from .buttons import MODULE_BUTTONS


class IndexView(AdminModuleView):

	""" Vista de configuracion """

	MODULE_NAME = "Configuracion"
	MODULE_HANDLER = ""
	template_name = 'configuracion/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context.update({
			"clientes": Cuenta.objects.filter(comunidad=self.comunidad, naturaleza__nombre="cliente").count(),
			"dominios": Cuenta.objects.filter(comunidad=self.comunidad, naturaleza__nombre="dominio").count(),
			"proveedores": Cuenta.objects.filter(comunidad=self.comunidad, naturaleza__nombre="proveedor").count(),
			"grupos": 0,
			"cajas": Cuenta.objects.filter(comunidad=self.comunidad, naturaleza__nombre="caja").count(),
			"ingresos": Cuenta.objects.filter(comunidad=self.comunidad, naturaleza__nombre="ingreso").count(),
			"gastos": Cuenta.objects.filter(comunidad=self.comunidad, naturaleza__nombre="gasto").count(),
			"intereses": Metodo.objects.filter(comunidad=self.comunidad, naturaleza="interes").count(),
			"descuentos": Metodo.objects.filter(comunidad=self.comunidad, naturaleza="descuento").count(),
			"titulos": Titulo.objects.filter(comunidad=self.comunidad).count(),
		})
		return context


class ListView(AdminModuleView):

	""" Vista de listado de cuentas, titulos y metodos """

	MODULE_NAME = "Configuracion"
	template_name = 'configuracion/list-objects.html'	
	MODULE_BUTTONS = MODULE_BUTTONS

	def get_context_data(self, **kwargs):
		self.MODULE_HANDLER = kwargs['naturaleza']
		context = super().get_context_data(**kwargs)
		context.update({"naturaleza": self.MODULE_HANDLER})
		return context

	