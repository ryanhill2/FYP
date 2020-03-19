# # from schedule import *
# import schedule
# import time
# from . import models
# from .models import Stock
#
#
# def createStockPrice():
#     inst = Stock.objects.all().last()
#     stock_ticker = inst.stock_ticker
#     value = getStockPrice(stock_ticker)
#
#     inst.stockCreated = value
#
#     inst.save()
#
#
# def getStockPrice(stockTicker):
#     df = web.DataReader(stockTicker, 'yahoo')
#     result = (df.tail(1))
#     result = result.values.tolist()
#     result = result[0][3]
#     result = round(result, 2)
#     return (result)
#
#
# def geeks():
#     print("Shaurya says Geeksforgeeks")
#
#
# schedule.every(1).seconds.do(geeks)
# # schedule.every(5).seconds.do(createStockPrice)
#
# # Loop so that the scheduling task
# # keeps on running all time.
# while True:
#     # Checks whether a scheduled task
#     # is pending to run or not
#     schedule.run_pending()
#     time.sleep(1)
