from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Shop, Category, Tag
from shop.forms import ShopForm


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()
    category_list = Category.objects.all()

    category_id = request.GET.get("category_id", "")
    if category_id:
        qs = qs.filter(category__pk=category_id)

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__icontains=query)

    context = {
        "shop_list": qs,
        "category_list": category_list,
    }
    return render(request, "shop/shop_list.html", context)


def shop_detail(request: HttpRequest, pk:int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    tag_list = shop.tag_set.all()
    context = {
        "shop": shop,
        "tag_list": tag_list,
    }
    return render(request, "shop/shop_detail.html", context)


def shop_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ShopForm(request.POST)
        if form.is_valid():
            saved_shop = form.save()
            return redirect("shop:shop_detail", saved_shop.pk)
    else:
        form = ShopForm()
    context = {
        "form": form,
    }
    return render(request, "shop/shop_form.html", context)


def shop_edit(request: HttpRequest, pk:int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == "POST":
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return redirect("shop:shop_detail", shop.pk)
    else:
        form = ShopForm(instance=shop)
    context = {
        "form": form,
    }
    return render(request, "shop/shop_form.html", context)
