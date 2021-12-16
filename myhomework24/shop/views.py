from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from shop.models import Shop, Tag, Comment, Category
from shop.forms import ShopForm, CommentForm


shop_list = ListView.as_view(
    model = Shop
)


shop_detail = DetailView.as_view(
    model = Shop
)

shop_new = CreateView.as_view(
    model = Shop,
    form_class = ShopForm,
)

shop_edit = UpdateView.as_view(
    model = Shop,
    form_class = ShopForm,
)

shop_delete = DeleteView.as_view(
    model = Shop,
)

comment_new = CreateView.as_view(
    model = Comment,
    form_class= CommentForm,
)

comment_edit = UpdateView.as_view(
    model = Comment,
    form_class= CommentForm,
)


comment_delete = DeleteView.as_view(
    model = Comment,
)
