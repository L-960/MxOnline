from django import forms
from apps.operations.models import UserFavorite


class UserFavForm(forms.ModelForm):
    class Meta:
        model = UserFavorite
        # 验证的字段
        fields = ["fav_id", "fav_type"]
