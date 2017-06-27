#coding:utf-8
import copy
class Prototype(object):
	def __init__(self, id, li):
		self.id = id
		self.li = li
	def clone(self):
		raise NotImplementedError
class ConcretePrototype(Prototype):
	def clone(self):
		return copy.copy(self)

if __name__ == '__main__':
	a = ConcretePrototype(123, ['a',['b','c']])
	b = a.clone()
	print a.id
	print a.li
	print b.id
	print b.li
	a.id = 345
	a.li[0] = 'd'
	print '-------------change-----------'
	print a.id
	print a.li
	print b.id
	print b.li