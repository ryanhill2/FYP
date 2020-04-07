import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
from mpl_finance import candlestick_ohlc
import mplfinance as mpf
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2019,5,8)
end = dt.datetime(2020,5,8)

df = web.DataReader('CRM', 'yahoo', start, end)
# first 6 values
# print(df.head(6))

# possibility to convert my data frame to a csv file
# df.to_csv('crm.csv')

#this will show all the filds this will result in a graph that is mostly taken up with the volume
# df.plot()
# plt.show()

# graph of the Adj close
# df['Adj Close'].plot()
# plt.show()


def AdjClose():
    df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
    df.dropna(inplace=True)

    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)

    ax1.plot(df.index, df['Adj Close'])
    plt.savefig('adjClose.png', dpi=100)
    plt.show()

def volume():
    ax2 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)

    ax2.bar(df.index, df['Volume'])
    plt.savefig('volume.png', dpi=100)
    plt.show()


# for 2 graps with three plots
def threeplots():
    df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
    df.dropna(inplace=True)

    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
    ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

    ax1.plot(df.index, df['Adj Close'])
    ax1.plot(df.index, df['100ma'])
    ax2.bar(df.index, df['Volume'])
    plt.savefig('multiChart.png', dpi=100)
    plt.show()


def candleStick():
    df_ohlc = df['Adj Close'].resample('10D').ohlc()
    df_volume = df['Volume'].resample('10D').sum()

    df_ohlc.reset_index(inplace=True)
    df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)


    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
    ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
    ax1.xaxis_date()

    candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
    ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)


    plt.savefig('candleStick.png', dpi=100)
    plt.show()


candleStick()
threeplots()
AdjClose()
volume()