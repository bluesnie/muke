# _*_ encoding: utf-8 _*_
__author__ = 'nzb'
__date__ = '2019/2/24 10:51'
from django import forms

from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    '''登录表单'''
    # 名称应与html中的name属性值相同
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=3)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=3)
    captcha = CaptchaField(error_messages={'invalid':u'验证码错误'})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid':u'验证码错误'})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=3)
    password2 = forms.CharField(required=True, min_length=3)