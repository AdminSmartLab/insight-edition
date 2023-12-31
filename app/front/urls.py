from django.urls import include, path

from .modules.base import BlankView
from . import views

urlpatterns = [

	# Front door
    path('', views.index, name='index'),

	# Generic Views
	path('pdf/<int:pk>/', views.PDFViewer.as_view(), name='pdf-viewer'),

	# System App Views
	path('cuentas-a-cobrar/', include(
		('front.modules.clientes.urls', 'clientes'), namespace='clientes')
	),
	path('cuentas-a-pagar/', include(
		('front.modules.proveedores.urls', 'proveedores'), namespace='proveedores')
	),
	path('tesoreria/', include(
		('front.modules.tesoreria.urls', 'tesoreria'), namespace='tesoreria')
	),
	path('stock/', include(
		('front.modules.stock.urls', 'stock'), namespace='stock')
	),	
	path('contabilidad/', include(
		('front.modules.contabilidad.urls', 'contabilidad'), namespace='contabilidad')
	),
	path('informes/', include(
		('front.modules.informes.urls', 'informes'), namespace='informes')
	),
	path('configuracion/', include(
		('front.modules.configuracion.urls', 'configuracion'), namespace='configuracion')
	),

	# Others
	path('perfil/', BlankView.as_view(), name='perfil'),
	path('biblioteca/', BlankView.as_view(), name='biblioteca'),

	path('change-community/', views.ChangeCommunity.as_view(), name='change-community'),

]
