# coding=utf-8
from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()


