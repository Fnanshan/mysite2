# coding=utf-8
# Create your models here.
from django.db import models


class PersonQuerySet(models.QuerySet):
    def public_authors(self):
        return self.filter(role='A')

    # 如果我创建了带有QuerySet的Manager,则Manager不能调用_开头的方法，；因为这是QuerySet的私有方法。
    # 相反，如果我用Manager调用自定义的QuerySet，则Manager可以调用_开头的方法，因为Manager调用QuerySet，由QuerySet调用私有方法。
    def _private_editors(self):
        return self.filter(role='E')


class PersonManager(models.Manager):
    def get_queryset(self):
        return PersonQuerySet(self.model, using=self._db)

    def authors(self):
        return self.get_queryset().public_authors()

    def editors(self):
        return self.get_queryset()._private_editors()


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=[('A', ('Author')), ('E', ('Editor'))])
    objects = models.Manager()
    people = PersonManager()
    # people = PersonQuerySet.as_manager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name