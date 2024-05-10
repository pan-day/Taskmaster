from django.db import models

class Task(models.Model):  # наследуем все от models от такого класса, как Model
    title = models.CharField('Название задачи', max_length=50)  # 1-ое поле title, текст до 255 символов - класс CharField
    task = models.TextField('Описание задачи')

    def __str__(self):  # сработает, когда попытаемся вывести обьект класса будет выводится не hash код, а title этого обьекта
        return self.title