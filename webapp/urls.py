from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # Test api
    url(r'^api/test', views.test_api, name='test_api'),

    url(r'^api/do_something', views.do_something, name='do_something'),

    url(r'^api/stock/get', views.stock, name='stock'),

    url(r'^api/stock/save', views.save_stock, name='save_stock'),

    url(r'^api/stock/all', views.all_stocks, name='all_stocks'),

    url(r'^api/stock/find', views.find_stock_by_code, name='find_stock_by_code'),

    url(r'^api/stockdata/import', views.import_stock_data, name='import_stock_data'),
]
