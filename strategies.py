import backtrader as bt

#Strategy
class first_strategy(bt.Strategy):
  params = (("fast_length",5),("slow_length", 25))
  def __init__(self):
    self.wma = bt.ind.SimpleMovingAverage(period=5)
    self.mma = bt.ind.SimpleMovingAverage(period = 20)
    self.cross = bt.ind.CrossOver(self.wma, self.mma)
  def next(self):
    if self.cross > 0:
      self.buy()
    elif self.cross < 0:
      self.close()
  def log(self,txt):
    pass
  def notify_order(self,order):
    pass