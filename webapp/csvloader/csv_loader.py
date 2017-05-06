import csv
from webapp.models import Stock
from webapp.models import StockData


def load(file_path, stock_id):
    """csvファイルの読み込みを行い、その結果をStockDataに詰めて返します"""
    result = []

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            stock_data = StockData(date_time=row[0], start=row[1], high=row[2], low=row[3], end=row[4], stock_id=Stock(id=stock_id))
            result.append(stock_data.to_dict())

    return result
