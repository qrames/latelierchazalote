# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .models import Article
# Create your views here.

class IndexView(TemplateView):
    template_name = "blog/index.html"
    # test test test
    # template_name = "blog/activity.html"
    # test test test


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
