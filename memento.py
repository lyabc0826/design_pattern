#coding:utf-8
class Originator(object):
	def __init__(self):
		self.state = None
	def create_memento(self):
		return Memento(self.state)
	def set_memento(self, m):
		self.state = m.state
	def show(self):
		print self.state
class Memento(object):
	def __init__(self, s):
		self.state = s
class CareTaker(object):
	def __init__(self):
		self.memento = None

if __name__ == '__main__':
	o = Originator()
	o.state = 'on'
	o.show()
	c = CareTaker()
	c.memento = o.create_memento()
	o.state = 'off'
	o.show()
	o.set_memento(c.memento)
	o.show()