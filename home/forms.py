from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài Khoản', max_length=30)
    email = forms.EmailField(label='Email')
    passworld1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    passworld2 = forms.CharField(label='Nhập Lại Mật Khẩu', widget=forms.PasswordInput())

    def clean_passworld2(self):
        if 'password1' in self.cleaned_data:
            passworld1 = self.cleaned_data['password1']
            passworld2 = self.cleaned_data['password2']
            if passworld1==passworld2 and passworld1:
                return passworld2
        raise forms.ValidationError("Mật Khẩu Không Hợp Lệ")
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError("Tên tài khoản có ký tự đặc biệt")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tên tài khoản có ký tự đặc biệt")
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['Email'], password=self.cleaned_data['password1'])