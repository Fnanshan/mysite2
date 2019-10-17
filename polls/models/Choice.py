# coding=utf-8
from django.db import models
from .Question import Question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # image = models.ImageField(width_field=300, height_field=200)

    def __str__(self):
        return self.choice_text