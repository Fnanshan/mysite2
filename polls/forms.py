# coding=utf-8

from django import forms
from django.forms import formset_factory

from polls.models import ArticleForm


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


'''学习Form代码'''
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


'''代码链接：
https://docs.djangoproject.com/zh-hans/2.2/ref/class-based-views/generic-editing/
https://docs.djangoproject.com/zh-hans/2.2/topics/forms/'''
'''表单实现“联系我”的功能'''
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        print('send_email~~~')


class ProductForm(forms.Form):
    name = forms.CharField()  # 名称
    num = forms.CharField()  # 编号
    spec = forms.CharField()  # 规格
    unit = forms.CharField()  # 单位
    price = forms.DecimalField()  # 价格
    remark = forms.CharField(widget=forms.Textarea)  # 说明

    def send_email(self):
        print('send_email~~~')


# formset_factory - build a formset of articles
# extra: 想要显示空表单的数量
# max_num: 表单显示最大数量，可选，默认1000
ArticleFormSet = formset_factory(ArticleForm, extra=3, max_num=2)