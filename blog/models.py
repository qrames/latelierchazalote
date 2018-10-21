# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='imageArticle')
    fk_article = models.ForeignKey('Article', on_delete=models.CASCADE)


STYLE_CHOICES = (
    ('primary', 'Style 1ere Importance'),
    ('secondary', 'Style secondaire'),
    ('default', 'Par defaut'),
)

PAGE_CHOICES = (
    ('cour-de-couture', 'Cour De Couture'),
    ('costumes-de-scenes', 'Costumes De Scenes'),
    ('creetion-sur-mesures', 'Creetion Sur Mesures'),
    ('atelier-de-creetion', 'Atelier De Creetion'),
    ('qui-suis-je', 'Ma presentation'),
)

class Article(models.Model):
    title = models.CharField(max_length = 200)
    page = models.CharField(max_length=200, choices=PAGE_CHOICES, default='qui-suis-je')
    style = models.CharField(max_length=200, choices=STYLE_CHOICES, default='default')
    texte = models.TextField()

    def __unicode__(self):
        return self.title
