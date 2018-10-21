# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Q

from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from extra_views import InlineFormSet, CreateWithInlinesView
from extra_views.generic import GenericInlineFormSet

from .models import Article, Image, STYLE_CHOICES, PAGE_CHOICES
# Create your views here.

class IndexView(TemplateView):
    template_name = "blog/index.html"


class ArticleView(ListView):
    model = Article

    def get_queryset(self, *args, **kwargs):
        print 'kwargs', self.kwargs, 'args', self.args

        return Article.objects.filter(Q(page__contains=self.kwargs['page']))


# ////////////////////////////////// PRIVITE WEBBACK:
class ImageInLine(InlineFormSet):
    model = Image
    fields = "__all__"


class ArticleFormSetView(CreateWithInlinesView):
    model = Article
    success_url = '/article'
    inlines = [
        ImageInLine,
    ]
    fields = "__all__"

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleFormSetView, self).get_context_data(**kwargs)
        context['style_choices'] = STYLE_CHOICES
        context['page_choices'] = PAGE_CHOICES

        return context
