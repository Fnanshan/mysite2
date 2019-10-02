# coding=utf-8
from django.db import models

from bookshop.models import Book


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name