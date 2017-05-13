from datetime import datetime
from django.test import TestCase, RequestFactory
from webapp.models import Stock
from webapp.models import StockData
import json

# Create your tests here.


class StockTest(TestCase):
    def test_stock_save(self):
        """Stockのオブジェクトを生成し、DBに登録できるかをテストします。"""
        s1 = Stock(name='日経平均株価', type='IX', code='NIKKEI225', createdDatetime=datetime.now().strftime("%Y/%m/%d %H:%M:%S"), version=0)
        s1.save()
        saved_stocks = Stock.objects.all()
        self.assertEqual(len(saved_stocks), 1)


class StockDataTest(TestCase):
    def test_stock_data_save(self):
        """StockDataのオブジェクトを生成し、DBに登録できるかをテストします（現在なぜか動かない）。"""
        s2 = Stock(name='日経平均株価', type='IX', code='NIKKEI225', createdDatetime=datetime.now().strftime("%Y/%m/%d %H:%M:%S"), version=0)
        s2.save()

        saved_stock_id = s2.id

        d = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        sd1 = StockData(date_time=d, start=120.0, high=150.0, low=110.0, end=200.0, stock_id=Stock(id=saved_stock_id))


class RestApiConnectionTest(TestCase):
    """APIの接続系の疎通確認テストを行います。"""
    def setUp(self):
        pass


    def test_connection_do_something(self):
        """do_somethingをテストします。"""
        response = self.client.get('/api/do_something')
        self.assertEqual(response.status_code, 200)


    def test_connection_all_stocks(self):
        """all_stocksをテストします"""
        pass


    def test_connection_find_stock(self):
        """findをテストします"""
        response = self.client.get('/api/stock/find')
        self.assertEqual(response.status_code, 200)


    def test_connection_import_stock_data(self):
        """インポートをテストします。"""
        response = self.client.post('/api/stockdata/import', { 'filename' : './webapp/csvloader/data/test.csv' })
        self.assertEqual(response.status_code, 200)


class RestApiDataTest(TestCase):
    """APIを通してデータの保存を行うテストを行います"""
    def setUp(self):
        """データベースにStockのデータが1つある状態にしておきます"""
        self.presave = Stock(name='日経平均株価', type='IX', code='NIKKEI225', createdDatetime=datetime.now().strftime("%Y/%m/%d %H:%M:%S"), version=0)
        self.presave.save()

        self.ok_filename = './webapp/csvloader/data/test.csv'

    def test_import_stock_data_ok(self):
        """テストデータから正常系インポートのロジックのテストを行います。"""
        response = self.client.post('/api/stockdata/import', { 'filename' : self.ok_filename, 'stock_id' : self.presave.id })
        result_dict = json.loads(response.content.decode('utf-8'))['data']
        result =[]

        for line in result_dict:
            stock_data = StockData()
            stock_data.to_obj(line)
            result.append(stock_data)

        self.assertEqual(len(result), 2)
