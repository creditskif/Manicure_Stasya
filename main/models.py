from django.db import models


class Price(models.Model):
    name = models.TextField('Название процедуры')
    price = models.TextField('Цена')

    def __str__(self):
        return self.name
