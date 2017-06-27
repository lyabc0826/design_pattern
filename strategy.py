#coding:utf-8
class Strategy(object):
	def __init__(self, num):
		self.num = num
	def process(self):
		raise NotImplementedError

class StrategyA(Strategy):
	def process(self):
		print self.num+1

class StrategyB(Strategy):
	def process(self):
		print self.num+2

class ScroEvent(object):
	def __init__(self, s):
		self.s = s
	def use_strategy(self, num):
		c = self.s
		print c
		inst = c(num)
		inst.process()

if __name__ == '__main__':
	s = ScroEvent(StrategyA)
	s.use_strategy(1)
	s2 = ScroEvent(StrategyB)
	s2.use_strategy(1)