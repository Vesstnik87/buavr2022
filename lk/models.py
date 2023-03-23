#import instance as instance
from django.db import models
from django.urls import reverse
from slugify import slugify
from uuslug import uuslug
from autoslug import AutoSlugField


def slugify_value(value):
    return value.replace(' ', '-')


def instance_slug(instance):
    return instance.slug

# СПИСОК ПРОФЕССИЙ
class Prof(models.Model): # СПИСОК ПРОФЕССИЙ
    prof = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.prof

# СПИСОК ПОДРАЗДЕЛЕНИЙ
class Group(models.Model): # СПИСОК ПОДРАЗДЕЛЕНИЙ, ГРУПП, СЛУЖБ
    group = models.CharField(max_length=30, null=True, blank=False)

    def __str__(self):
        return self.group

# ДИАМЕТРЫ ГАЗОПРОВОДА
class Diametr(models.Model): # ДИАМЕТР ТРУБЫ
    d_gazopr = models.TextField()

    def __str__(self):
        return self.d_gazopr

# УЧАСТОК ГАЗОПРОВОДА
class Uchastok(models.Model):
    file_prikaz = models.FileField('prikaz/', null=True)
    prikaz_number = models.CharField(max_length=100, verbose_name='№ совместного приказа', null=True)
    prikaz_date = models.DateField(verbose_name='Дата совместного приказа', null=True)
    file_razresh = models.FileField('razreshenie/', null=True)
    razresh_number = models.CharField(max_length=100, verbose_name='№ разрешения', null=True)
    razresh_date = models.DateField(verbose_name='Дата разрешения', null=True)
    lpu = models.ForeignKey('Lpumg', on_delete=models.PROTECT, verbose_name='Наименование филиала ЛПУМГ', null=True)
    nitka = models.ForeignKey('Gazopr', on_delete=models.PROTECT, verbose_name='Наименование газопровода', null=True)
    d_gazopr = models.ForeignKey('Diametr', on_delete=models.PROTECT, verbose_name='Диаметр газопровода',
        blank=True, null=True)
    start_uch = models.FloatField(null=True, verbose_name='Начало участка')
    end_uch = models.FloatField(null=True, verbose_name='Конец участка')
    status_uch = models.BooleanField(default=False, blank=True,  verbose_name='Статус участка') # Ремонт/Работа
    date_start_razresh = models.DateField(verbose_name='Дата начала', null=True)
    date_end_razresh = models.DateField(verbose_name='Дата окончания', null=True)
    date_start_plan = models.DateField(verbose_name='Дата начала', null=True)
    date_end_plan = models.DateField(verbose_name='Дата начала', null=True)
    kol_trub_plan = models.IntegerField(null=True, verbose_name='Кол. труб по плану')
    kol_trub_fakt = models.IntegerField(null=True, verbose_name='Кол. труб по факту')
    date_start_fact = models.DateField(verbose_name='Дата начала по факту', null=True)
    date_end_fact = models.DateField(verbose_name='Дата окончания по факту', null=True)
    slug = AutoSlugField('URL', max_length=100, db_index=True, unique=True, populate_from=instance_slug,
        slugify=slugify_value, null=True)
    distant_location = models.BooleanField(verbose_name='Отдаленный участок')
    davleniye = models.BooleanField(verbose_name='Участок сниженного давления', default=False)
    dlina_uchastka = models.FloatField(verbose_name='Длина участка', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = uuslug(str(self.nitka), instance=self) + '-' + uuslug(str(self.start_uch),
            instance=self) + '-' + uuslug(str(self.end_uch), instance=self)
        super(Uchastok, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.nitka)+' '+str(self.start_uch)+'-'+str(self.end_uch)


    def get_absolute_url(self):
        return reverse('remont_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Участок'
        verbose_name_plural = 'Участки'
        ordering = ['nitka', 'start_uch', 'end_uch']

# СПИСОК ОТДЕЛЕНИЙ
class Otdel(models.Model): # ОТДЕЛЕНИЕ
    otdel = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.otdel

# СПИСОК ФИЛИАЛОВ
class Lpumg(models.Model): # СПИСОК ЛПУ
    lpumg = models.CharField(max_length=100)

    def __str__(self):
        return self.lpumg

# СПИСОК ГАЗОПРОВОДОВ
class Gazopr(models.Model): # СПИСОК ГАЗОПРОВОДОВ
    gazopr = models.CharField(max_length=255)

    def __str__(self):
        return self.gazopr

# СПИСОК ВОЗМОЖНЫХ ДЕФФЕКТОВ
class Deffect(models.Model):
    deffect = models.CharField(max_length=255, db_index=True)


    def __str__(self):
        return self.deffect

# СПИСОК ТЕХНИКИ
class Tehnika(models.Model):
    model = models.CharField(max_length=255, verbose_name='Модель техники', null=True)
    gos_number = models.SlugField(max_length=100, verbose_name='Гос.номер', null=True)
    icon = models.CharField(max_length=100, verbose_name='Изображение', null=True)
    status = models.CharField(max_length=155, verbose_name='Статус', null=True)
    location1 = models.CharField(max_length=100, null=True, blank=True, verbose_name='Местоположение 1')
    location2 = models.IntegerField(null=True, blank=True, verbose_name='Труба')
    type = models.CharField(max_length=255, verbose_name='Тип техники')
    driver = models.ForeignKey('Personal', on_delete=models.PROTECT, verbose_name='Водитель', null=True, blank=True)
    rashod_h = models.FloatField(verbose_name='Расход ч.', null=True, blank=True)
    rashod_km = models.FloatField(verbose_name='Расход км.', null=True, blank=True)
    prinadlejnost = models.CharField(max_length=100, null=True, blank=True, verbose_name='Принадлежность')
    inv_number = models.CharField(max_length=100, null=True, blank=True, verbose_name='Инв.номер')
    teh_1 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Резервное поле')
    teh_2 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Резервное поле')
    teh_3 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Резервное поле')
    teh_4 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Резервное поле')
    teh_5 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Резервное поле')

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'
        ordering = ['type', 'model', 'gos_number', 'status', 'location1', 'location2', 'rashod_h', 'rashod_km']

# СПИСОК МЕСТОПОЛОЖЕНИЙ
class Locations(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Местоположение')
    slug = models.SlugField()
    dop_1 = models.CharField(max_length=150, null=True, blank=True, verbose_name='доп1')
    dop_2 = models.CharField(max_length=150, null=True, blank=True, verbose_name='доп2')
    dop_3 = models.CharField(max_length=150, null=True, blank=True, verbose_name='доп3')
    dop_4 = models.CharField(max_length=150, null=True, blank=True, verbose_name='доп4')
    dop_5 = models.CharField(max_length=150, null=True, blank=True, verbose_name='доп5')

# МЕТОДЫ РЕМОНТА
class Metod_remonta(models.Model):
    met_remont = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.met_remont


# СПИСОК УЧАСТКОВ АВР
class Uchavr(models.Model):
    uchavr = models.CharField(max_length=30, null=True, blank=False)

    def __str__(self):
        return self.uchavr

# ТРУБА
class Truba(models.Model):
    number = models.IntegerField(verbose_name= 'Номер трубы', null=True, blank=True)
    dlina = models.FloatField(verbose_name='Длина трубы', null=True, blank=True)
    stenka = models.FloatField(verbose_name='Толщина стенки', null=True, blank=True)
    construkciya = models.CharField(max_length=50, verbose_name='Конструкция трубы', null=True, blank=True)
    int_psh = models.CharField(verbose_name='Входящий ПШ', max_length=100, null=True, blank=True)
    out_psh = models.CharField(verbose_name='Исходящий ПШ', max_length=100, null=True, blank=True)
    otvod = models.BooleanField(verbose_name='Отвод', blank=True)
    otvod_type = models.CharField(verbose_name='Тип отвода', max_length=100, null=True, blank=True)
    otvod_segment = models.IntegerField(verbose_name='Число сегментов отвода', null=True, blank=True)
    otvod_izgib = models.FloatField(verbose_name='Угол изгиба в Град.', null=True, blank=True)
    otvod_proekciya = models.CharField(verbose_name='Угол в проекции Град.', max_length=100, null=True, blank=True)
    otvod_napravleniye = models.CharField(verbose_name='Направление', max_length=100, null=True, blank=True)
    danger = models.CharField(verbose_name='Опасность', max_length=50, null=True, blank=True)
    dop_8734653748 = models.CharField(max_length=150, null=True, blank=True, verbose_name='дополнительное поле')


    def_1 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Вид деффекта')
    def_1_type_rem = models.CharField(max_length=255, null=True, blank=True, verbose_name='Метод ремонта')
    def_1_compl_rem = models.CharField(max_length=255, null=True, blank=True, verbose_name='')
    def_1_dop_1 = models.CharField(max_length=255, verbose_name='Дополнительное поле', null=True, blank=True)
    def_1_dop_2 = models.CharField(max_length=255, verbose_name='Дополнительное поле', null=True, blank=True)
    def_1_dop_3 = models.CharField(max_length=255, verbose_name='Дополнительное поле', null=True, blank=True)
    def_1_dop_4 = models.CharField(max_length=255, verbose_name='Дополнительное поле', null=True, blank=True)
    def_1_dop_5 = models.CharField(max_length=255, verbose_name='Дополнительное поле', null=True, blank=True)
    def_1_dop_6 = models.CharField(max_length=255, verbose_name='Дополнительное поле', null=True, blank=True)
    def_1_dop_7 = models.CharField(max_length=255, verbose_name='Дополнительное поле', null=True, blank=True)
    def_1_dop_8 = models.CharField(max_length=255, verbose_name='Дополнительное поле', null=True, blank=True)
    def_1_dop_9 = models.CharField(max_length=255, verbose_name='Дополнительное поле', null=True, blank=True)
    def_1_dop_10 = models.CharField(max_length=255, verbose_name='Дополнительное поле', null=True, blank=True)
    def_1_percent = models.IntegerField(null=True, verbose_name='Процент дефекта', blank=True)
    def_1_piket = models.FloatField(null=True, verbose_name='Пикетаж', blank=True)
    def_1_km = models.FloatField(null=True, verbose_name='Километр', blank=True)

    def_2 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Вид деффекта')
    def_2_type_rem = models.CharField(max_length=255, null=True, blank=True, verbose_name='Метод ремонта')
    def_2_compl_rem = models.CharField(max_length=255, null=True, blank=True, verbose_name='Метод ремонта')
    def_2_dop_1 = models.CharField(max_length=255, verbose_name='Дополнительное поле', null=True, blank=True)
    def_2_dop_2 = models.CharField(max_length=255, verbose_name='Дополнительное поле', null=True, blank=True)
    def_2_dop_3 = models.CharField(max_length=255, verbose_name='Дополнительное поле', null=True, blank=True)
    def_2_dop_4 = models.CharField(max_length=255, verbose_name='Дополнительное поле', null=True, blank=True)
    def_2_dop_5 = models.CharField(max_length=255, verbose_name='Дополнительное поле', null=True, blank=True)
    def_2_dop_6 = models.CharField(max_length=255, verbose_name='Дополнительное поле', null=True, blank=True)
    def_2_dop_7 = models.CharField(max_length=255, verbose_name='Дополнительное поле', null=True, blank=True)
    def_2_dop_8 = models.CharField(max_length=255, verbose_name='Дополнительное поле', null=True, blank=True)
    def_2_dop_9 = models.CharField(max_length=255, verbose_name='Дополнительное поле', null=True, blank=True)
    def_2_dop_10 = models.CharField(max_length=255, verbose_name='Дополнительное поле', null=True, blank=True)
    def_2_percent = models.IntegerField(null=True, verbose_name='Процент дефекта', blank=True)
    def_2_piket = models.FloatField(null=True, verbose_name='Пикетаж', blank=True)
    def_2_km = models.FloatField(null=True, verbose_name='Километр', blank=True)

    stage_works = models.ForeignKey('Status', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Этап работ')
    zaglushka_sever = models.BooleanField(default=False, verbose_name='Заглашка с северной стороны', blank=True)
    zaglushka_ug = models.BooleanField(default=False, verbose_name='Заглушка с южной стороны', blank=True)
    peremichka_up = models.BooleanField(default=False, verbose_name='Перемычка вверх', blank=True)
    peremichka_down = models.BooleanField(default=False, verbose_name='Перемычка вниз', blank=True)
    comment_1 = models.TextField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
    comment_2 = models.TextField(max_length=30, null=True, blank=True, verbose_name='Комментарий')
    comment_3 = models.TextField(max_length=30, null=True, blank=True, verbose_name='Комментарий')


    uch_trub = models.ForeignKey('Uchastok', on_delete=models.PROTECT, verbose_name='Принадлежность к участку', blank=True)
    uch_trubid = models.IntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("test_truba", kwargs={"int": self.number})


    class Meta:
        verbose_name = 'Труба'
        verbose_name_plural = 'Трубы'
        ordering = ['number', 'uch_trub']


# СТАТУСЫ/ЭТАП РАБОТ
class Status(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Этап работ")

    def __str__(self):
        return self.name


# УЧЕТ СВАРНЫХ
class Svarshov(models.Model):
    name = models.CharField(max_length=100, null=True)


# ПЕРСОНАЛ
class Personal(models.Model):
    name_1 = models.CharField(max_length=255, verbose_name='Фамилия')
    name_2 = models.CharField(max_length=255,verbose_name='Имя')
    name_3 = models.CharField(max_length=255, verbose_name='Отчество')
    bithday = models.DateField(verbose_name='Дата рождения', null=True)
    ustroen = models.DateField(verbose_name='Дата трудоустройства')
    tabnumber = models.IntegerField(verbose_name='Табельный номер')
    professiya = models.ForeignKey('Prof', on_delete=models.PROTECT, verbose_name='Профессия', null=True)
    lvl = models.IntegerField(null=True, verbose_name='Разряд')
    gruppa = models.ForeignKey('Group', on_delete=models.PROTECT, verbose_name='Подразделение')
    uch_avr = models.ForeignKey('Uchavr', on_delete=models.PROTECT, null=True, verbose_name='Участок', blank=True)
    otdeleniye = models.ForeignKey('Otdel', on_delete=models.PROTECT, null=True, verbose_name='Отделение', blank=True)
    slug = AutoSlugField('URL', max_length=100, db_index=True, unique=True, populate_from=instance_slug,
                         slugify=slugify_value)
    examen_ot = models.DateField(verbose_name='Проверка знаний по ОТ', null=True, blank=True)
    next_examen_ot = models.DateField(verbose_name='Проверка знаний по ОТ', null=True, blank=True)
    examen_eb = models.DateField(verbose_name='Проверка знаний по ЭБ', null=True, blank=True)
    next_examen_eb = models.DateField(verbose_name='Проверка знаний по ЭБ', null=True, blank=True)
    examen_ptm = models.DateField(verbose_name='ПТМ', null=True, blank=True)
    next_examen_ptm = models.DateField(verbose_name='ПТМ', null=True, blank=True)
    examen_pdd = models.DateField(verbose_name='ПДД', null=True, blank=True)
    next_examen_pdd = models.DateField(verbose_name='ПДД', null=True, blank=True)
    instructaj = models.DateField(verbose_name='Инструктаж', null=True, blank=True)
    med_osmotr = models.DateField(verbose_name='Мед.осмотр', null=True, blank=True)
    flura = models.DateField(verbose_name='Флюорография', null=True, blank=True)
    otpusk_start = models.DateField(verbose_name='Осн.отпуск', null=True, blank=True)
    otpusk_end = models.DateField(verbose_name='Осн.отпуск', null=True, blank=True)
    otpusk_d1_start = models.DateField(verbose_name='Доп.отпуск', null=True, blank=True)
    otpusk_d1_end = models.DateField(verbose_name='Доп.отпуск', null=True, blank=True)
    otpusk_d2_start = models.DateField(verbose_name='Доп.отпуск', null=True, blank=True)
    otpusk_d2_end = models.DateField(verbose_name='Доп.отпуск', null=True, blank=True)
    location_1 = models.CharField(verbose_name='Местоположение 1', max_length=255, null=True, blank=True)
    location_2 = models.CharField(verbose_name='Местоположение 2', max_length=255, null=True, blank=True)
    foto = models.ImageField(upload_to='avatar/', help_text='150х150', verbose_name='Фото сотрудника', null=True, blank=True)
    ssz = models.BooleanField(verbose_name='ССЗ', default=False)

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name_1, instance=self) + '-' + uuslug(self.name_2, instance=self) + '-' + uuslug(self.name_3, instance=self)
        super(Personal, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("card_user", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'
        ordering = ['name_1', 'name_2']


# УЧЕТ РАБОЧЕГО ВРЕМЕНИ
class RabTime(models.Model):
    name = models.ForeignKey('Tehnika', on_delete=models.PROTECT, verbose_name="Техника")
    date = models.DateField()
    time_start = models.TimeField()
    time_finish = models.TimeField()