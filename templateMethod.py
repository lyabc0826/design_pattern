#coding:utf-8
class AbstractClass(object):
	def method1(self):
		raise NotImplementedError
	def method2(self):
		raise NotImplementedError
	def process(self):
		self.method1()
		self.method2()
		print "end"

class ConcreteClass1(AbstractClass):
	def method1(self):
		print "I am class one and method one"
	def method2(self):
		print "I am class one and method two"

class ConcreteClass2(AbstractClass):
	def method1(self):
		print "I am class two and method one"
	def method2(self):
		print "I am class two and method two"

if __name__ == '__main__':
	c1 = ConcreteClass1()
	c1.process()
	c2 = ConcreteClass2()
	c2.process()
