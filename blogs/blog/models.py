from django.db import models
from markdownx.models import MarkdownxField

class Tag(models.Model):
    name = models.CharField('タグ名', max_length=255, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('タイトル', max_length=32)
    text = MarkdownxField('本文')
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name='カテゴリ')
    tags = models.ManyToManyField(Tag, verbose_name='タグ', blank=True)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = MarkdownxField('本文')
    target = models.ForeignKey(
        Post, on_delete=models.PROTECT, verbose_name='どの記事のコメントか')

    def __str__(self):
        return self.text[:20]
