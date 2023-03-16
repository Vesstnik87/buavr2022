import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'buavr2022.settings'

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import django
django.setup()
from xlrd import open_workbook
import xlrd
import uuid
from random import randint
from lk.models import *

class UploadingTrub(object):
	foreign_key_fields = ['uch_trub', 'status']
	model = Truba

	def __init__(self, data):
		data = data
		self.uploaded_file = data.get('file')
		self.parsing()

	def getting_related_model(self, field_name):
		related_model = self.model._meta.get_field(field_name).rel.to
		return related_model

	def getting_headers(self):
		s = self.s
		headers = dict()
		for column in range(s.ncols):
			value = s.cell(0, column).value
			headers[column] = value
		return headers

	def parsing(self):
		uploading_file = self.uploaded_file
		wb = xlrd.open_workbook(file_contents=uploading_file.read())
		s = wb.sheet_by_index(0)
		self.s = s

		headers = self.getting_headers()
		print(headers)

		truba_bulk_list  = list()
		for row in range(1, s.nrows):
			row_dict = {}
			for column in range(s.ncols):
				value = s.cell(row, column).value
				field_name = headers[column]


				if field_name == 'id' and not value:
					continue

				if field_name in self.foreign_key_fields:
					related_model = self.getting_related_model(field_name)
					print(related_model)

					instance, created = related_model.objects.get_or_create(name=value)
					value = instance

				row_dict[field_name] = value

			print(row_dict)
			truba_bulk_list.append(Truba(**row_dict))
			# Truba.objects.create(**row_dict)
		Truba.objects.bulk_created(truba_bulk_list)
		return True