from django.contrib import admin
from admincu.operative.models import Operacion
from import_export.admin import ImportExportMixin


class OperacionAdmin(ImportExportMixin, admin.ModelAdmin):
	list_display = ['cuenta', 'valor']
	list_filter = ['comunidad', 'cuenta__naturaleza']

admin.site.register(Operacion, OperacionAdmin)
