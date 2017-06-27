#coding:utf-8

class SystemOne(object):
	def method_one(self):
		print "method one"

class SystemTwo(object):
	def method_two(self):
		print "method two"

class SystemThree(object):
	def method_three(self):
		print "method three"

class Facade(object):
	def __init__(self):
		self.s_1 = SystemOne()
		self.s_2 = SystemTwo()
		self.s_3 = SystemThree()
	def method_a(self):
		self.s_1.method_one()
		self.s_2.method_two()
	def method_b(self):
		self.s_1.method_one()
		self.s_2.method_two()

if __name__=='__main__':
	f = Facade()
	f.method_a()
	f.method_b()