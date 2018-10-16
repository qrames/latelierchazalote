# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='imageArticle')
    fk_article = models.ForeignKey('Article', on_delete=models.CASCADE)

class Article(models.Model):
    title = models.CharField(max_length = 200)
