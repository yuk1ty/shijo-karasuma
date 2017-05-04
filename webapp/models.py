from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Stock(models.Model):
    MARKET_CHOICES = (
        (u'IX', u'Index'),
        (u'ID', u'Individual'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=2, choices=MARKET_CHOICES)
    code = models.CharField(max_length=50)
    createdDatetime = models.DateTimeField(auto_now=True)
    version = models.IntegerField(default=0)


class StockDate(models.Model):
    id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(auto_now=False)
    start = models.FloatField
    high = models.FloatField
    low = models.FloatField
    end = models.FloatField
    stock = models.ForeignKey(Stock)
