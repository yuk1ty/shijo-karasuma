import json
from datetime import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from webapp.models import Stock
from webapp.csvloader import csv_loader


def index(request):
    return render(request, 'webapp/index.html', {})

@csrf_exempt
def test_api(request):
    return JsonResponse({'foo': 'bar'})

@csrf_exempt
def do_something(request):
    return JsonResponse({ 'message' : '反応してないの？' })

@csrf_exempt
def stock(request):
    return JsonResponse({
      'id': '1',
      'name': 'Nikkei 225',
      'code': 'NI225',
      'stockData':  [{
        'id': '1',
        'date': '2017-05-04',
        'time': '09:00:00.000',
        'start': '19400.00',
        'high': '19500.00',
        'low': '19200.00',
        'end': '19450.00',
      },{
        'id': '2',
        'date': '2017-05-04',
        'time': '12:00:00.000',
        'start': '194500.00',
        'high': '19500.00',
        'low': '19200.00',
        'end': '19400.00'
      },{
        'id': '3',
        'date': '2017-05-04',
        'time': '15:00:00.000',
        'start': '19400.00',
        'high': '19550.00',
        'low': '19200.00',
        'end': '19550.00'
      }]
    })


@csrf_exempt
def save_stock(request):
    data = json.loads(request.body.decode("utf-8"))['data']
    to_register = Stock(name = data['name'], type = __convert_type(data['type']), code = data['code'], createdDatetime = datetime.strptime(data['createdDateTime'], '%Y-%m-%d %H:%M:%S'), version=0)
    to_register.save()
    return JsonResponse({ 'message' : '成功しました' })

def __convert_type(type):
    if type == "Index":
        return "IX"
    elif type == "Individual":
        return "ID"
    else:
        return ""


@csrf_exempt
def all_stocks(request):
    print(request)


@csrf_exempt
def find_stock_by_code(request):
    print(request)


@csrf_exempt
def import_stock_data(request):
    print(request)
    # 一旦サンプルでdataを入れる
    result = csv_loader.load('data/test.csv')
