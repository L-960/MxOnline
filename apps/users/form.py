from django import forms


# 对在表单中获取到的username和password进行处理
class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)
