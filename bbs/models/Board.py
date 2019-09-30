from django.db import models
# coding=utf-8


class Board(models.Model):
    boardid = models.AutoField('板块自动编号', primary_key=True)
    boardname = models.CharField('版块名称', max_length=200)
    boardtopics = models.IntegerField('版块主题数', default=0)
    boardmanager = models.CharField('版主名', max_length=200)
    boardintroduce = models.CharField('板块介绍', max_length=200, default='')

    class Meta:
        db_table = "Board"

    def __str__(self):
        return self.boardname

    def get_absolute_url(self):
        return "/bbs/%i/" % self.boardid