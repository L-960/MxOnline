from django import forms
from apps.operations.models import *


class UserFavForm(forms.ModelForm):
    class Meta:
        model = UserFavorite
        # 验证的字段
        fields = ["fav_id", "fav_type"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = CourseComments
        fields = ["course", "comments"]
