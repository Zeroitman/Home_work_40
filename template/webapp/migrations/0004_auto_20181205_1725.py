# Generated by Django 2.1.3 on 2018-12-05 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20181204_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
        migrations.RemoveField(
            model_name='task',
            name='due_date',
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование задачи'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, default='new', max_length=20, verbose_name='Статус задачи'),
        ),
    ]