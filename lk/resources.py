from  import_export import resources
from .models import *


class TrubaResources(resources.ModelResource):

	class Meta:
		model = Truba


class PersonalResource(resources.ModelResource):

	class Meta:
		model = Personal


class UchastokResource(resources.ModelResource):

	class Meta:
		model = Uchastok


class TehnikaResource(resources.ModelResource):

	class Meta:
		model = Tehnika