from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from .models import *


class PersonalResource(resources.ModelResource):

	class Meta:
		model = Personal


class PersonalAdmin(ImportExportActionModelAdmin):
	list_display = (
		'id', 'name_1', 'name_2',
		'name_3', 'ustroen', 'tabnumber',
		'professiya', 'gruppa')
	search_fields = ('name_2',)
	list_display_links = ('id', 'name_1', 'name_2', 'name_3')
	resource_class = PersonalResource


class UchastokResource(resources.ModelResource):

	class Meta:
		model = Uchastok


class UchastokAdmin(ImportExportActionModelAdmin):
	list_display = (
		'id', 'lpu', 'nitka', 'start_uch', 'end_uch')
	search_fields = ('nitka',)
	list_display_links = ('id', 'lpu', 'nitka')


class TehnikaResource(resources.ModelResource):

	class Meta:
		model = Tehnika


class TehnikaAdmin(ImportExportActionModelAdmin):
	list_display = (
		'id', 'type', 'model', 'gos_number', 'rashod_h', 'status', 'icon', 'rashod_km'
	)


class TrubaResource(resources.ModelResource):

	class Meta:
		model = Truba


class TrubaAdmin(ImportExportActionModelAdmin):
	resource_class = TrubaResource
	list_display = ('id', 'number', 'dlina', 'otvod', 'def_1', 'def_1_percent', 'comment_1', 'comment_2', 'uch_trub')
	list_display_links  = ('number', 'uch_trub')

admin.site.register(Truba, TrubaAdmin)
admin.site.register(Uchastok, UchastokAdmin)
admin.site.register(Personal, PersonalAdmin)
admin.site.register(Tehnika, TehnikaAdmin)