# Generated by Django 4.0.4 on 2022-12-23 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0006_locations_alter_tehnika_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truba',
            name='comment_1',
            field=models.TextField(blank=True, max_length=20, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='comment_2',
            field=models.TextField(blank=True, max_length=20, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='truba',
            name='comment_3',
            field=models.TextField(blank=True, max_length=20, null=True, verbose_name='Комментарий'),
        ),
    ]
