# Generated by Django 4.0.4 on 2022-12-22 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0005_alter_tehnika_options_tehnika_location_sity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Местоположение')),
                ('slug', models.SlugField()),
                ('dop_1', models.CharField(blank=True, max_length=150, null=True, verbose_name='доп1')),
                ('dop_2', models.CharField(blank=True, max_length=150, null=True, verbose_name='доп2')),
                ('dop_3', models.CharField(blank=True, max_length=150, null=True, verbose_name='доп3')),
                ('dop_4', models.CharField(blank=True, max_length=150, null=True, verbose_name='доп4')),
                ('dop_5', models.CharField(blank=True, max_length=150, null=True, verbose_name='доп5')),
            ],
        ),
        migrations.AlterModelOptions(
            name='tehnika',
            options={'ordering': ['type', 'model', 'gos_number', 'status', 'location1', 'location2', 'rashod'], 'verbose_name': 'Техника', 'verbose_name_plural': 'Техника'},
        ),
        migrations.RemoveField(
            model_name='tehnika',
            name='location',
        ),
        migrations.RemoveField(
            model_name='tehnika',
            name='location_sity',
        ),
        migrations.RemoveField(
            model_name='truba',
            name='tehnika',
        ),
        migrations.AddField(
            model_name='tehnika',
            name='location1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Местоположение 1'),
        ),
        migrations.AddField(
            model_name='tehnika',
            name='location2',
            field=models.IntegerField(blank=True, null=True, verbose_name='Местоположение 2'),
        ),
        migrations.AddField(
            model_name='truba',
            name='dop_8734653748',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='construkciya',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Конструкция трубы'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='danger',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Опасность'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_1_dop_1',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_1_dop_10',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_1_dop_2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_1_dop_3',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_1_dop_4',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_1_dop_5',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_1_dop_6',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_1_dop_7',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_1_dop_8',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_1_dop_9',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_1_km',
            field=models.FloatField(blank=True, null=True, verbose_name='Километр'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_1_percent',
            field=models.IntegerField(blank=True, null=True, verbose_name='Процент дефекта'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_1_piket',
            field=models.FloatField(blank=True, null=True, verbose_name='Пикетаж'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_2_dop_1',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_2_dop_10',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_2_dop_2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_2_dop_3',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_2_dop_4',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_2_dop_5',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_2_dop_6',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_2_dop_7',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_2_dop_8',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_2_dop_9',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_2_km',
            field=models.FloatField(blank=True, null=True, verbose_name='Километр'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_2_percent',
            field=models.IntegerField(blank=True, null=True, verbose_name='Процент дефекта'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='def_2_piket',
            field=models.FloatField(blank=True, null=True, verbose_name='Пикетаж'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='dlina',
            field=models.FloatField(blank=True, null=True, verbose_name='Длина трубы'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='int_psh',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Входящий ПШ'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер трубы'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='otvod',
            field=models.BooleanField(blank=True, verbose_name='Отвод'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='otvod_izgib',
            field=models.FloatField(blank=True, null=True, verbose_name='Угол изгиба в Град.'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='otvod_napravleniye',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Направление'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='otvod_proekciya',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Угол в проекции Град.'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='otvod_segment',
            field=models.IntegerField(blank=True, null=True, verbose_name='Число сегментов отвода'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='otvod_type',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Тип отвода'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='out_psh',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Исходящий ПШ'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='peremichka_down',
            field=models.BooleanField(blank=True, default=False, verbose_name='Перемычка вниз'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='peremichka_up',
            field=models.BooleanField(blank=True, default=False, verbose_name='Перемычка вверх'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='stenka',
            field=models.FloatField(blank=True, null=True, verbose_name='Толщина стенки'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='uch_trub',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='lk.uchastok', verbose_name='Принадлежность к участку'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='uch_trubid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='truba',
            name='zaglushka_sever',
            field=models.BooleanField(blank=True, default=False, verbose_name='Заглашка с северной стороны'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='zaglushka_ug',
            field=models.BooleanField(blank=True, default=False, verbose_name='Заглушка с южной стороны'),
        ),
        migrations.CreateModel(
            name='RabTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_start', models.TimeField()),
                ('time_finish', models.TimeField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lk.tehnika', verbose_name='Техника')),
            ],
        ),
    ]
