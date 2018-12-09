from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=80, verbose_name='Наименование задачи')
    status = models.BooleanField(null=False, default=False, verbose_name='Статус задачи')

    def __str__(self):
        return f"{self.pk}, {self.name},({self.status})"



