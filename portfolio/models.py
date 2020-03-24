from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Stock(models.Model):
    stock_ticker = models.TextField(max_length=5)
    purchase_price = models.TextField(max_length=100, blank=True)
    current_price = models.TextField(max_length=100, blank=True)
    stock_change = models.TextField(max_length=100, blank=True)
    number_of_shares = models.TextField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stockCreated = models.DateTimeField(auto_now_add=True)
    stockUpdated = models.DateTimeField(auto_now=True)

    daily_high = models.TextField(max_length=10)
    daily_low = models.TextField(max_length=10)
    daily_open = models.TextField(max_length=10)
    daily_close = models.TextField(max_length=10)
    stock_volume = models.TextField(max_length=10)
    daily_adj_close = models.TextField(max_length=10)


    def __str__(self):
        return self.stock_ticker


# class Portfolio(models.Model):
#     portfolio_name = models.TextField(max_length=10)
#     # stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
#
#     portfolioCreated = models.DateTimeField(auto_now_add=True)
#     portfolioUpdated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.portfolio_name

class Portfolio(models.Model):
    portfolio_name = models.TextField(max_length=10)
    # stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    date = models.TextField(max_length=10)
    stocks = models.ManyToManyField(Stock)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_change = models.TextField(max_length=10)

    def __str__(self):
        return self.portfolio_name

class Transactions(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    trans_stock_ticker = models.TextField(max_length=100)
    stock_price = models.TextField(max_length=100)
    date_logged = models.DateTimeField(auto_now=True)








