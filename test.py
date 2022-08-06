from datetime import datetime
import backtrader as bt
import yfinance as yf
from strategies import *

#Create cerebro and add strategy
cerebro = bt.Cerebro()
cerebro.addstrategy(first_strategy)

#Date feed
data = bt.feeds.PandasData(dataname = yf.download('2330.TW','2015-1-1','2021-1-1'))
cerebro.adddata(data)
cerebro.broker.setcash(1000000)
print(cerebro.broker.get_value())
cerebro.run()
print(cerebro.broker.get_value())
cerebro.plot()
