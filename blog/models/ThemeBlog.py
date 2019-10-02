# coding=utf-8
from django.db import models

from blog.models.Blog import Blog


class ThemeBlog(Blog):
    theme = models.CharField(max_length=200)