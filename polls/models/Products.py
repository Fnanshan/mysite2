# coding=utf-8
from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=120, verbose_name='名称')
    num = models.CharField(max_length=60, verbose_name='编号')
    spec = models.CharField(max_length=200, verbose_name='规格')
    unit = models.CharField(max_length=20, verbose_name='单位')
    price = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='价格')
    remark = models.CharField(max_length=500, verbose_name='说明')

    def __str__(self):
        return self.name
