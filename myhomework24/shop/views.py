from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from shop.models import Shop, Tag, Comment, Category
from shop.forms import ShopForm, CommentForm


class ShopListView(ListView):
    model = Shop

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q", "").strip()
        if q:
            qs = qs.filter(name__icontains=q)
        return qs


shop_list = ShopListView.as_view()


shop_detail = DetailView.as_view(
    model=Shop,
)

shop_new = CreateView.as_view(
    model=Shop,
    form_class=ShopForm,
)

shop_edit = UpdateView.as_view(
    model=Shop,
    form_class=ShopForm,
)

shop_delete = DeleteView.as_view(
    model=Shop,
    success_url=reverse_lazy("shop:shop_list"),
)

comment_new = CreateView.as_view(
    model=Comment,
    form_class=CommentForm,
)

comment_edit = UpdateView.as_view(
    model=Comment,
    form_class=CommentForm,
)

comment_delete = DeleteView.as_view(
    model=Comment,
    # TODO : 삭제 성공시 post_detail로 돌아가기
    success_url=reverse_lazy("shop:shop_list"),
)
