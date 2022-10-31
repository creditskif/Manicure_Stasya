from django.db import models


class Price(models.Model):
    name = models.TextField('Название процедуры')
    price = models.TextField('Цена')

    def __str__(self):
        return '%s (%s)' % (self.name, self.price)


class Plan(models.Model):
    date = models.DateField('Дата работы')
    time = models.TimeField('Время')

    def __str__(self):
        return '%s (%s)' % (self.date, self.time)


class Recording(models.Model):
    date = models.DateField('Дата работы')
    time = models.TimeField('Время')
    procedure = models.TextField('Процедура')
    fi = models.TextField('Фамилия и Имя')
    phone = models.TextField('Номер телефона')

    def __str__(self):
        return '%s - %s  %s  %s' % (self.date, self.time, self.fi, self.phone)