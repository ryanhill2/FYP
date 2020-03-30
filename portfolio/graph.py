import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2016,1,1)

df = web.DataReader('CRM', 'yahoo', start, end)
# first 6 values
print(df.head(6))