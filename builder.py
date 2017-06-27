#coding:utf-8
class Product(object):
	def __init__(self):
		self.parts = []
	def add(self, part):
		self.parts.append(part)
	def show(self):
		print self.parts

class Builder(object):
	def __init__(self):
		self.product = Product()
	def build_partA(self):
		raise NotImplementedError
	def build_partB(self):
		raise NotImplementedError
	def get_result(self):
		return self.product

class ConcretebuiilderA(Builder):
	def build_partA(self):
		self.product.add('part one')
	def build_partB(self):
		self.product.add('part two')

class ConcretebuiilderB(Builder):
	def build_partA(self):
		self.product.add('part three')
	def build_partB(self):
		self.product.add('part four')

class Director(object):
	def __init__(self, b):
		b.build_partA()
		b.build_partB()

if __name__ == '__main__':
	c_a = ConcretebuiilderA()
	c_b = ConcretebuiilderB()
	d_a = Director(c_a)
	p_a = c_a.get_result()
	p_a.show()
	d_b = Director(c_b)
	p_b = c_b.get_result()
	p_b.show()

		
