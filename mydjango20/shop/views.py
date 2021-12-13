from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from shop.forms import ShopForm, ReviewForm
from shop.models import Shop, Review, Tag, Category


#/
def shop_main(request:HttpRequest) -> HttpResponse:
    tag_list = Tag.objects.all()
    context = {"tag_list": tag_list}
    return render(request,"shop/shop_main.html", context)


# /list/
def shop_list(request:HttpRequest) -> HttpResponse:
    qs = Shop.objects.all() #order_by("_id")
    tag_list = Tag.objects.all()
    category_qs = Category.objects.all()
    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__icontains=query)

    category_id: str = request.GET.get("category_id", "")
    if category_id:
        qs = qs.filter(category__pk=category_id)

    return render(request, "shop/shop_list.html", {
        "shop_list": qs,
        "tag_list": tag_list,
        "category_list": category_qs,
    })


# /shop/100/
def shop_detail(request:HttpRequest, pk:int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    review_list = shop.review_set.all()
    tag_list = shop.tag_set.all()
    return render(request, "shop/shop_detail.html", {
        "shop": shop,
        "review_list": review_list,
        "tag_list": tag_list,
    })


def tag_detail(request: HttpRequest, tag_name:str) -> HttpResponse:
    qs = Shop.objects.all()
    qs = qs.filter(tag_set__name=tag_name)
    tag_list = Tag.objects.all()

    return render(request, "shop/tag_detail.html", {
        "shop_list": qs,
        "tag_list": tag_list,
    })


# /shop/new/
def shop_new(request: HttpRequest) -> HttpResponse:
    # raise NotImplementedError("곧 구현 예정")
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post = form.save()
            # shop_detail 뷰를 구현 했다면 !!!
            return redirect("shop:shop_detail", saved_post.pk)
    else:
        form = ShopForm()

    return render(request, "shop/shop_new.html", {
        "form": form,
    })


# /shop/edit/"number"
def shop_edit(request: HttpRequest, shop_pk:int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=shop_pk)

    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            saved_post = form.save()
            return redirect("shop:shop_detail", saved_post.pk)
    else:
        form = ShopForm(instance=shop)

    return render(request, "shop/shop_new.html", {
        "form": form,
    })


def review_new(request: HttpRequest, shop_pk:int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=shop_pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.shop = shop
            review.save()
            return redirect("shop:shop_detail", shop_pk)
    else:
        form = ReviewForm()

    return render(request, "shop/review_form.html", {
        "form": form,
    })


def review_edit(request: HttpRequest, shop_pk:int, pk:int) -> HttpResponse:
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect("shop:shop_detail", shop_pk)
    else:
        form = ReviewForm(instance=review)

    return render(request, "shop/review_form.html", {
        "form": form,
    })
