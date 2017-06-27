#coding:utf-8

class Component(object):
	def  __init__(self, name):
		self.name = name
	def add(self, c):
		raise NotImplementedError
	def remove(self, c):
		raise NotImplementedError
	def display(self, depth):
		raise NotImplementedError

class Leaf(Component):
	def add(self, c):
		print 'not support add'
	def remove(self, c):
		print 'not support add'
	def display(self, depth):
		print '-'*depth+self.name

class Composite(Component):
	def  __init__(self, name):
		super(Composite, self).__init__(name)
		self.com_list = []
	def add(self, c):
		self.com_list.append(c)
	def remove(self, c):
		self.com_list.remove(c)
	def display(self, depth):
		print '-'*depth+self.name
		for item in self.com_list:
			item.display(depth+1)

if __name__ == '__main__':
	root = Composite('root')
	a = Leaf('A')
	root.add(a)
	root.add(Leaf('B'))
	x = Composite('X')
	x.add(Leaf('XA'))
	x.add(Leaf('XB'))
	root.add(x)
	root.display(1)








