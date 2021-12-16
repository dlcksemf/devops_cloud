from django.contrib import admin
from blog.forms import PostForm
from blog.models import Post, Comment, Category, Tag, Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

