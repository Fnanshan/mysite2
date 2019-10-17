# coding=utf-8

from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


'''代码链接：https://docs.djangoproject.com/zh-hans/2.2/ref/class-based-views/generic-editing/'''


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

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
