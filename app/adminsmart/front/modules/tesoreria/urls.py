from django.urls import path

from ..base import BlankView

from .views import *

urlpatterns = [

	# Custom Views
	path('', IndexView.as_view(), name='index'),

	# Estados
	path('estados/<int:pk>/deuda/', EstadoDeudasView.as_view(), name='estado-deudas'), # Stockeables 
	path('estados/<int:pk>/cuenta/', EstadoCuentaView.as_view(), name='estado-cuenta'),

	# Cuenta
	path('cuenta/create/', CUDObjectView.as_view(), name='create'),
	path('cuenta/edit/<int:pk>/', CUDObjectView.as_view(), name='cuenta'),

	# Comprobantes
	path('cbte/', BlankView.as_view(), name='cbte-create'),
	path('cbte/<int:pk>', BlankView.as_view(), name='cbte-edit'),

	# Registros
	path('registros/', RegistroView.as_view(), name='registros'),
	
	# PreOperaciones
	path('pre-operaciones/', BlankView.as_view(), name='pre-operaciones'),	

	# PreOperaciones
	path('cbte-masivo/', BlankView.as_view(), name='cbte-masivo'),		

	


]


