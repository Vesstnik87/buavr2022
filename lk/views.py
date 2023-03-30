from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, JsonResponse, request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.db.models import Q
from .utils import *
from .models import *
from lk.forms import RegisterPersonal, VivodUchastka
from .resources import *
from tablib import Dataset

class GroupUchavr:
    def get_groups(self):
        return Group.objects.all()

    def get_uchavrs(self):
        return Uchavr.objects.all()

    def get_professiya(self):
        return  Prof.objects.all()

    def get_familiya(self):
        return Personal.objects.all()

    def get_otdels(self):
        return Otdel.objects.all()

    def get_hron(self):
        return Hron.objects.all()

class GroupUchastok:
    def get_lpumg(self):
        return Lpumg.objects.all()
    def get_nitka(self):
        return Gazopr.objects.all()
    def get_d_gazopr(self):
        return Diametr.objects.all()
    def get_truba(self):
        return Truba.objects.all()


# ВЫВОД СПИСКА РАБОТНИКОВ
class PersonList(GroupUchavr, ListView):
    """Спиок работников"""
    model = Personal
    queryset = Personal.objects.all()
    extra_context = {
        'title': 'Сотрудники',
        'url_name': 'Регистрация работника'
    }


# ВЫВОД СПИСКА РЕМОНТИРУЕМЫХ УЧАСТКОВ
class RemontUcastki(ListView):
    model = Uchastok
    # queryset = Uchastok.objects.all()
    extra_context = {'title': 'Ремонты', 'url_name': 'Вывод участка в ремонт', 'url_name_2': 'Текущие ремонты'}


# ИНОФРМАЦИЯ ПО РЕМОНТИРУЕМОМУ УЧАСТКУ
class RemontDetail(DetailView, GroupUchastok):
    model = Uchastok
    slug_field = "slug"
    # pk_url_kwarg = 'uch_pk'
    extra_context = {'title': 'Ремонты', 'url_name': 'Вывод участка в ремонт', 'url_name_2': 'Текущие ремонты'}

# ВЫВОД РЕМОНТИРУЕМЫХ ТРУБ
def getTrump(request):
    truba = Truba.objects.all()
    return JsonResponse( {"truba": list(truba.values())} )




# ВЫВОД ТЕХНИКИ 
def getTehnika(request):
    tehnika = Tehnika.objects.all()
    return JsonResponse( {"tehnika": list(tehnika.values())} )

# ЗАГРУЗКА ФАЙЛА ВТД
def upload_vtd(request):
    if request.method == 'POST':
        truba_resource = TrubaResources()
        dataset = Dataset()
        new_truba = request.FILES['vtd']

        imported_data = dataset.load(new_truba.read())
        result = truba_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            truba_resource.import_data(dataset, dry_run=False)

    # return redirect('remonti')
    return redirect('remonti')

# ИНСТРУКТАЖИ, ЭКЗАМЕНЫ, ОХРАНА ТРУДА
class OhranaTruda(GroupUchavr, ListView):
    model = Personal
    queryset = Personal.objects.all()
    template_name = 'lk/ohrana_truda.html'
    extra_context = {'title': 'Охрана труда'}


# ФИЛЬТР РАБОТНИКОВ
class PersonalFilter(GroupUchavr, ListView):
    extra_context = {
        'title': 'Сотрудники',
        'url_name': 'Регистрация работника',
        'url_name_2': 'Удаление работника из БД'}

    def get_queryset(self):
        queryset = Personal.objects.all()
        # if "name_1" in self.request.GET:
        #     queryset = queryset.filter(name_1__in=self.request.GET.getlist("name_1"))
        if "uchavr" in self.request.GET:
            queryset = queryset.filter(uch_avr__in=self.request.GET.getlist("uchavr"))
        if "group" in self.request.GET:
            queryset = queryset.filter(gruppa__in=self.request.GET.getlist("group"))
        if "professiya" in self.request.GET:
            queryset = queryset.filter(professiya__in=self.request.GET.getlist("professiya"))
        return queryset


# ЛИЧНАЯ КАРТОЧКА РАБОТНИКА
class CardUser(GroupUchavr, DetailView):
    model = Personal
    slug_field = "slug"
    extra_context = {'title': 'Карточка работника'}


def base(request):
    return render(request, 'lk/base.html', {'title': 'Проверка базового шаблона'})


def home(request):
    return render(request, 'lk/home.html', {
        'title': 'Домашняя страница',
        'url_name_1': 'Текущие ремонты'
    })


# РЕГИСТРАЦИЯ РАБОТНИКА
class RegPers(GroupUchavr, CreateView):
    form_class = RegisterPersonal
    template_name = 'lk/register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация работника'
        context['url_name'] = 'Список сотрудников'
        return context


# ВЫВОД УЧАСТКА В РЕМОНТ
class AddUch(CreateView, GroupUchastok):
    form_class = VivodUchastka
    template_name = 'lk/vivod_uchastka.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вывод участка в ремонт'
        context['url_name_2'] = 'Текущие ремонты'
        return context


# РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЕЙ
class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'lk/register_user.html'
    success_url = reverse_lazy('author')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

class UserUpdate(UpdateView, GroupUchavr):
    model = Personal
    template_name = 'lk/personal_update.html'
    fields = [
        'name_1', 'name_2', 'name_3', 'tabnumber', 'bithday',
        'ustroen', 'uch_avr', 'professiya', 'otdeleniye', 'gruppa', 'examen_ot',
        'examen_eb', 'examen_pdd', 'examen_ptm', 'instructaj', 'otpusk_start',
        'otpusk_end', 'otpusk_d1_start', 'otpusk_d1_end', 'otpusk_d2_start',
        'otpusk_d2_end', 'foto'
    ]


# АВТОРИЗАЦИЯ
class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'lk/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return  context

    def get_success_url(self):
        return reverse_lazy('remonti')



