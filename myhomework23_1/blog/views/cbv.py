from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from blog.models import Post
from blog.forms import PostForm


post_list = ListView.as_view(
    model = Post,
)

post_detail = DetailView.as_view(
    model = Post,
)

post_new = CreateView.as_view(
    model = Post,
    form_class = PostForm,
)

post_edit = UpdateView.as_view(
    model = Post,
    form_class = PostForm,
)

post_delete = DeleteView.as_view(
    model = Post,
    success_url=reverse_lazy("blog:post_list"),
)