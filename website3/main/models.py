from django.db import models

class Task(models.Model):
    title = models.CharField('Название',max_length=50)
    task = models.TextField('Описание')
    user = models.CharField('Пользователь',max_length=100)
    date = models.DateField('Дата')

    def __str__(self):
        return self.title