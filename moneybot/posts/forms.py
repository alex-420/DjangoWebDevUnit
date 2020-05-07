from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        fields = ("content", "forum")
        model = models.Post

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["forum"].queryset = (
                models.Forum.objects.filter(
                    pk__in=user.forums.values_list("forum__pk")
                )
            )
