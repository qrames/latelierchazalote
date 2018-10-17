# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from extra_views import InlineFormSet, CreateWithInlinesView
from extra_views.generic import GenericInlineFormSet

from .models import Article, Image
# Create your views here.

class IndexView(TemplateView):
    template_name = "blog/index.html"
    # test test test
    # template_name = "blog/activity.html"
    # test test test

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


class ArticleView(ListView):
    model = Article

class CourDeCouture(ArticleView):
    template_name = "blog/cour-de-couture.html"


class CostumesDeScenes(ArticleView):
    pass

class CreetionSurMesures(ArticleView):
    pass

class atelierDeCreetion(ArticleView):
    pass
