from django.db.models.signals import post_save
from django.dispatch import receiver
from portfolio.models import Stock, Portfolio
import schedule
import time

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

import pandas_datareader.data as web


def add(x, y):
    return x + y


@receiver(post_save, sender=Stock)
def createStockPrice(sender, instance, created, **kwargs):
    if created:
        stock_ticker = instance.stock_ticker
        current_price = (getCurrentPrice(stock_ticker))
        var = (getStockPrice(stock_ticker))
        high = getStockHigh(stock_ticker)
        low = getStockLow(stock_ticker)
        open = getStockOpen(stock_ticker)
        close = getStockClose(stock_ticker)
        volume = getStockVolume(stock_ticker)
        adjclose = getStockADJclose(stock_ticker)

        instance.current_price = current_price
        instance.daily_high = high
        instance.daily_low = low
        instance.daily_open = open
        instance.daily_close = close
        instance.stock_volume = volume
        instance.daily_adj_close = adjclose

        instance.purchase_price = var

        instance.save()

        stocks = Stock.objects.all()
        stockTotal = 0.0
        stockPrice = 0.0
        quantity = 0


        for stock in stocks:
            stockPrice = stockPrice + float(stock.purchase_price)
            quantity = quantity + int(stock.number_of_shares)
            stockTotal = stockTotal + (stockPrice * quantity)

            stockTotal = round(stockTotal, 2)
            print(stockTotal)

        portfolios = Portfolio.objects.all()
        for portfolio in portfolios:
            print(stockTotal)
            print(portfolio.total_change)
            portfolio.total_change = stockTotal
            print(portfolio.total_change)
            portfolio.save()





def getStockPrice(stockTicker):
    df = web.DataReader(stockTicker, 'yahoo')
    result = (df.tail(1))
    result = result.values.tolist()
    result = result[0][3]
    result = round(result, 2)
    return (result)


def getCurrentPrice(stockTicker):
    df = web.DataReader(stockTicker, 'yahoo')
    result = (df.tail(1))
    result = result.values.tolist()
    result = result[0][3]
    result = round(result, 2)
    return (result)

def getStockHigh(stockTicker):
    df = web.DataReader(stockTicker, 'yahoo')
    result = (df.tail(1))
    result = result.values.tolist()
    result = result[0][0]
    result = round(result, 2)
    return (result)


def getStockLow(stockTicker):
    df = web.DataReader(stockTicker, 'yahoo')
    result = (df.tail(1))
    result = result.values.tolist()
    result = result[0][1]
    result = round(result, 2)
    return (result)


def getStockOpen(stockTicker):
    df = web.DataReader(stockTicker, 'yahoo')
    result = (df.tail(1))
    result = result.values.tolist()
    result = result[0][2]
    result = round(result, 2)
    return (result)


def getStockClose(stockTicker):
    df = web.DataReader(stockTicker, 'yahoo')
    result = (df.tail(1))
    result = result.values.tolist()
    result = result[0][3]
    result = round(result, 2)
    return (result)


def getStockVolume(stockTicker):
    df = web.DataReader(stockTicker, 'yahoo')
    result = (df.tail(1))
    result = result.values.tolist()
    result = result[0][4]
    result = round(result, 2)
    return (result)


def getStockADJclose(stockTicker):
    df = web.DataReader(stockTicker, 'yahoo')
    result = (df.tail(1))
    result = result.values.tolist()
    result = result[0][5]
    result = round(result, 2)
    return (result)

def updateStockPrice():
    r = getListOfStocks()
    for val in r:
        print(val)
        getCurrentPrice(val)


def getListOfStocks():
    listOfAllStocks = Stock.objects.all()
    for stock in listOfAllStocks:
        p = stock.stock_ticker

        listofStocks = set()

        listofStocks.add(p)
        print(listofStocks)
    return listofStocks





    # print(listOfStocks)
#
#
# style.use('ggplot')
#
# start = dt.datetime(2000, 1, 1)
# end = dt.datetime(2019, 11, 7)
# stock_name = 'ANF'
#
# df = web.DataReader(stock_name, 'yahoo')
# print(df.tail(6))

# schedule.every(1).seconds.do(updateStockPrice)
# while True:
#     schedule.run_pending()
#     time.sleep(1)