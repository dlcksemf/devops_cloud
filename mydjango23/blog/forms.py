from django import forms
from blog.models import Post, Comment, Tag


class PostForm(forms.ModelForm):
    tags = forms.CharField()

    # 초기값 지정
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            tag_qs = self.instance.tag_set.all()
            tags = ", ".join([tag.name for tag in tag_qs])
            self.fields["tags"].initial = tags

    # 아래의 함수가 호출 되기 전에, instance.save()가 호출되었음을 보장받습니다.
    # manytomany인 상황에서 instance pk가 있음을 확인 받기
    def _save_m2m(self):
        saved_post = super()._save_m2m()
        tag_list = []
        tags = self.cleaned_data.get("tags", "")
        for word in tags.split(","):
            tag_name = word.strip()
            tag, __ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)

        self.instance.tag_set.clear()
        self.instance.tag_set.add(*tag_list)


    class Meta:
        model = Post
        fields = [
            "title",
            "category",
            "content",
            "photo",
            "status"
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"