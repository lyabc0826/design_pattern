#coding:utf-8

class State(object):
	def handle(self, context):
		raise NotImplementedError

class ConcreteStateA(State):
	def handle(self, context):
		context.state = ConcreteStateB()
		print context.state

class ConcreteStateB(State):
	def handle(self, context):
		context.state = ConcreteStateA()
		print context.state

class Context(object):
	def __init__(self):
		self.state = ConcreteStateA()

	def request(self):
		self.state.handle(self)

if __name__ == '__main__':
	c = Context()
	c.request()
	c.request()
	c.request()
	c.request()