# _*_encoding: utf-8 _*_

__author__ = 'nzb'
__date__ = '2019/2/27 11:01'

import re
from django import forms

from operation.models import UserAsk

# 传统的form
#
# class UserAskForm(forms):
#     name = forms.CharField(required=True, min_length=2, max_length=20)
#     phone = forms.CharField(required=True, min_length=11, max_length=11)
#     course_name = forms.CharField(required=True, min_length=5, max_length=50)


# 使用Django带的modelform
class UserAskForm(forms.ModelForm):
    # 还可以增加自定义字段
    # myfields = forms.CharField(...)
    class Meta:
        model = UserAsk
        fields = ['name', 'tel', 'course_name']

    def clean_tel(self):
        """
        验证手机号是否合法
        :return:
        """
        tel = self.cleaned_data['tel']
        TEL_REGEXP = "^1([38][0-9]|4[579]|5[0-3,5-9]|6[6]|7[0135678]|9[89])\d{8}$"
        p = re.compile(TEL_REGEXP)
        if p.match(tel):
            return tel
        else:
            raise forms.ValidationError(u'手机号非法', code='tel_invalid')