from django.shortcuts import resolve_url
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import PostForm
from blog.models import Post

# Class Based View(CBV)
#    - 뷰 함수를 만들어주는 클래스

# post_list
post_list = ListView.as_view(
    model=Post,
)

# post_detail
post_detail = DetailView.as_view(
    model=Post,
)


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    # success_url = reverse_lazy("blog:post_list")

    # def get_success_url(self):
        # self.object # 저장된 모델 인스턴스
        # post_pk = self.object.pk
        # return reverse("blog:post_detail", args=[post_pk]) # 문자열
        # return resolve_url("blog:post_detail", post_pk) # 문자열
        # return redirect("blog:post_detail", post_pk) # HttpResponse
        # {% url "blog:post_detail" post_pk %} # 문자열


# post_new
post_new = PostCreateView.as_view()


# post_edit
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    # def get_success_url(self):
    #     post_pk = self.object.pk
    #     return reverse("blog:post_detail", args=[post_pk]) # 문자열


post_edit = PostUpdateView.as_view()


# post_delete
post_delete = DeleteView.as_view(
    model = Post,
    success_url=reverse_lazy("blog:post_list"),
)