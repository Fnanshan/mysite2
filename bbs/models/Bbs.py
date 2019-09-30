from django.db import models
from .Board import Board
# Create your models here.


class Bbs(models.Model):
    bbsid = models.AutoField('帖子自动编号', primary_key=True)
    boardid = models.ForeignKey(Board, on_delete=models.CASCADE)
    parentid = models.IntegerField('父贴编号', default=None)
    child = models.IntegerField('跟帖数', default=None)
    username = models.CharField('发表人姓名', max_length=100)
    expression = models.CharField('发帖人E-mail', max_length=100)
    bbstitle = models.CharField('发表人标题', max_length=200)
    bbscontent = models.TextField('文章内容')
    dateandtime = models.DateTimeField('文章发表时间')
    bbsclick = models.IntegerField('论坛点击率', default=0)
    # bbshot = models.BinaryField('是否为精华帖', default=False)
    bbshot = models.IntegerField('是否为精华帖', default=0)

    class Meta:
        db_table = "Bbs"

    def get_absolute_url(self):
        return "/bbs/%i/" % self.bbsid