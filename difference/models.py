from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TextDifferenceModel(models.Model):
    original = models.TextField(max_length=1000000000,blank=False)
    changed = models.TextField(max_length=1000000000,blank=False)
