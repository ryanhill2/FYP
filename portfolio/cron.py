from .signals import updateStockPrice
def my_cron_job():
    updateStockPrice()

my_cron_job()
