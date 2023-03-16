from tkinter import Widget
from django import forms
from .models import *


# Форма регистрации нового работника
class RegisterPersonal(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['professiya'].empty_label ='Профессия не выбрана'
		self.fields['gruppa'].empty_label = 'Подразделение не выбрано'
		self.fields['uch_avr'].empty_label = 'Участок не выбран'
		self.fields['otdeleniye'].empty_label = 'Отделение не выбрано'
		# self.fields['slug'].prepopulated_fields = ("name_1", "name_2", "name_3")
	class Meta:
		model = Personal
		fields = ['name_1', 'name_2', 'name_3', 'ustroen', 'tabnumber', 'professiya', 'lvl', 'gruppa', 'uch_avr', 'otdeleniye', 'bithday']

# Форма вывода участка в ремонт
class VivodUchastka(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['lpu'].empty_label = 'ЛПУ МГ не выбрано'
		self.fields['nitka'].empty_label = 'Газопровод не выбран'
		self.fields['d_gazopr'].empty_label = 'Диаметр газопровода не выбран'

	class Meta:
		model = Uchastok
		fields = [
			'lpu', 'nitka', 'd_gazopr', 'start_uch', 'end_uch',
			'razresh_date',  'razresh_number', 'date_start_razresh',
			'date_end_razresh', 'kol_trub_plan', 'date_start_plan',
			'date_end_plan', 'date_start_fact', 'date_end_fact']
		widgets = {
			'lpu': forms.Select(attrs={'class': 'input'}),
			'nitka': forms.Select(attrs={'class': 'input'}),
			'd_gazopr': forms.Select(attrs={'class': 'input'}),
			'start_uch': forms.NumberInput(attrs={'class': 'input'}),
			'end_uch': forms.NumberInput(attrs={'class': 'input'}),
			'razresh_date': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),
			'razresh_number': forms.NumberInput(attrs={'class': 'input'}),
			'date_start_razresh': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),
			'date_end_razresh': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),
			'kol_trub_plan': forms.NumberInput(attrs={'class': 'input'}),
			'date_start_plan': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),
			'date_end_plan': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),
			'date_start_fact': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),
			'date_end_fact': forms.DateInput(attrs={'class': 'input', 'type': 'date'})
		}

# class DetailTruba(forms.ModelForm):
# 	def __init__(self, *args, **kwargs):
# 		super().__init__(*args, **kwargs)
# 		self.fields['stage_works'].empty_label ='Не определен'
# 		self.fields['def_1'].empty_label = 'Не выбрано'
# 		self.fields['def_2'].empty_label = 'Не выбрано'
# 		self.fields['def_3'].empty_label = 'Не выбрано'
# 		self.fields['def_1_type_rem'].empty_label = 'Не выбрано'
# 		self.fields['def_1_type_rem'].empty_label = 'Не выбрано'
# 		self.fields['def_1_type_rem'].empty_label = 'Не выбрано'
#
# 	class Meta:
# 		model = Truba
# 		fields = [
# 			'number', 'dlina', 'stenka', 'construkciya', 'int_psh ', 'out_psh', 'otvod',
# 			'otvod_type', 'otvod_segment', 'otvod_izgib', 'otvod_proekciya', 'otvod_napravleniye'
# 			'danger', 'def_1', 'def_1_type_rem', 'def_1_compl_rem', 'def_1_percent', 'def_1_piket'
# 			'def_1_km', 'stage_works', 'zaglushka_sever', 'zaglushka_ug', 'peremichka_up',
# 			'peremichka_down', 'comment_1',
# 		]