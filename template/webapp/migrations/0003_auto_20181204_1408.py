# Generated by Django 2.1.3 on 2018-12-04 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20181204_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(null=True, verbose_name='Выполнить к'),
        ),
    ]