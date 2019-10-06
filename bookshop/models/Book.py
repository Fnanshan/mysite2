# coding=utf-8
from django.db import models

from bookshop.models import Author, Publisher


# First, define the Manager subclass.
class DahlBookManager(models.Manager):
    def get_queryset(self):
        # 调用父类的成员语法为：super().方法名
        return super().get_queryset().filter(authors__name='Roald Dahl')


class secondBookManager(models.Manager):
    def get_queryset(self):
        return 'this is secondBookManager'


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()

    # objects = models.Manager()  # The default manager.
    # dahl_objects = DahlBookManager()  # The Dahl-specific manager.
    # second_objects = secondBookManager()

    def __str__(self):
        return self.name
