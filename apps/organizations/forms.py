from django import forms


class AddAskForm(forms.ModelForm):
    # 对表单中name为mobile的字段进行限制
    mobile = forms.CharField(max_length=11, required=True)

    class Meta:
        pass
