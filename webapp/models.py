from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.forms.models import model_to_dict

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

    def to_dict(self):
        """JSONオブジェクトへの変換のために、このクラスを辞書型にして返します。"""
        return model_to_dict(self)


class StockData(models.Model):
    id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField(auto_now=True)
    start = models.FloatField(default=0)
    high = models.FloatField(default=0)
    low = models.FloatField(default=0)
    end = models.FloatField(default=0)
    stock_id = models.ForeignKey(Stock)

    def to_dict(self):
        """JSONオブジェクトへの変換のために、このクラスを辞書型にして返します。"""
        return {
            'id':self.id,
            'date_time':self.date_time,
            'start':self.start,
            'high':self.high,
            'low':self.low,
            'end':self.end,
            'stock_id':self.stock_id.to_dict()
        }

    def to_obj(self, source_dict):
        """JSONオブジェクトから、Pythonクラスへの変換を行います。"""
        return StockData(date_time=datetime.strptime(source_dict['date_time'], '%Y-%m-%d %H:%M:%S'), start=source_dict['start'], high=source_dict['high'], low=source_dict['low'], end=source_dict['end'])
