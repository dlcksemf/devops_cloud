from django.contrib.auth.mixins import UserPassesTestMixin


class ReviewUserCheckMixin(UserPassesTestMixin):
    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user


class ShopOwnerCheckMixin(UserPassesTestMixin):
    def test_func(self):
        shop = self.get_object()
        return self.request.user == shop.owner