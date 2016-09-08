from django.db import models
import json
import re

# Create your models here.

ref_re = re.compile(r'\^|\\u\d+|u[\'\"]|[\'\"]')

class Page(models.Model):
    classification = models.CharField(max_length=30)
    title = models.CharField(max_length=30, default='')
    content = models.CharField(max_length=3000)
    references = models.CharField(max_length=1000, default='[]')
    page_id=models.IntegerField(primary_key=True, default=1)


class Word(models.Model):
    idx = models.CharField(max_length=30, primary_key=True)
    index_table = models.CharField(max_length=3000)
