from datetime import datetime
from django.test import TestCase
from webapp.models import Stock
from webapp.models import StockData

# Create your tests here.


class StockTest(TestCase):
    def test_stock_save(self):
        s1 = Stock(name='日経平均株価', type='IX', code='NIKKEI225', createdDatetime=datetime.now().strftime("%Y/%m/%d %H:%M:%S"), version=0)
        s1.save()
        saved_stocks = Stock.objects.all()
        print("test_stock_save_id: " + str(s1.id))


class StockDataTest(TestCase):
    def test_stock_data_save(self):
        s2 = Stock(name='日経平均株価', type='IX', code='NIKKEI225', createdDatetime=datetime.now().strftime("%Y/%m/%d %H:%M:%S"), version=0)
        s2.save()

        print("id: " + str(s2.id))
        saved_stock_id = s2.id

        # なんかうまく動かない
        d = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        sd1 = StockData(date_time=d, start=120.0, high=150.0, low=110.0, end=200.0, stock_id=Stock(id=saved_stock_id))
