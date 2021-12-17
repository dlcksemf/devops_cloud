from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import resolve_url, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from shop.mixins import ReviewUserCheckMixin, ShopOwnerCheckMixin
from shop.models import Category, Shop, Review, Tag
from shop.forms import ShopForm, ReviewForm


class ShopListView(ListView):
    model=Shop

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["category_list"] = Category.objects.all()
        return context_data

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("query", "").strip()
        if query:
            qs = qs.filter(name__icontains=query)
        return qs


shop_list = ShopListView.as_view()

shop_detail = DetailView.as_view(
    model=Shop,
)


class ShopCreateView(LoginRequiredMixin, CreateView):

    model = Shop
    form_class = ShopForm

    # 유효성 검사에 통과 하면 호출 되는 함수
    def form_valid(self, form) -> HttpResponse:
        # self.kwargs : URL Captured 값들이 사전으로 저장
        shop = form.save(commit=False)
        shop.owner = self.request.user
        shop.save()
        return redirect(shop)
        # return super().form_valid(form)


shop_new = ShopCreateView.as_view()


class ShopUpdateView(LoginRequiredMixin, ShopOwnerCheckMixin, UpdateView):
    model=Shop
    form_class=ShopForm


shop_edit = ShopUpdateView.as_view()


class ShopDeleteView(LoginRequiredMixin, ShopOwnerCheckMixin, DeleteView):
    model=Shop
    success_url=reverse_lazy('shop:shop_list')


shop_delete = ShopDeleteView.as_view()


class ReviewCreateView(LoginRequiredMixin, CreateView):

    model = Review
    form_class = ReviewForm

    # 유효성 검사에 통과 하면 호출 되는 함수
    def form_valid(self, form) -> HttpResponse:
        # self.kwargs : URL Captured 값들이 사전으로 저장
        shop = get_object_or_404(Shop, pk=self.kwargs['shop_pk'])
        review = form.save(commit=False)
        review.shop = shop
        review.user = self.request.user
        review.save()
        return redirect(shop)
        # return super().form_valid(form)

    # def get_success_url(self):
    #     return resolve_url('shop:shop_detail', self.kwargs['shop_pk'])


review_new = ReviewCreateView.as_view()


class ReviewUpdateView(LoginRequiredMixin, ReviewUserCheckMixin, UpdateView):
    model = Review
    form_class = ReviewForm

    def get_success_url(self):
        review = self.object
        return resolve_url(review.shop)


review_edit = ReviewUpdateView.as_view()


class ReviewDeleteView(LoginRequiredMixin, ReviewUserCheckMixin, DeleteView):
    model = Review

    def get_success_url(self):
        review = self.object
        return resolve_url(review.shop)


review_delete = ReviewDeleteView.as_view()
