# Generated by Django 2.1.3 on 2018-12-05 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20181205_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Статус задачи'),
        ),
    ]
