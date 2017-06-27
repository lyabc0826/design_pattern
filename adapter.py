#coding:utf-8

class Target(object):
	def request(self):
		print "I am common request"

class Adaptee(object):
	def specific_request(self):
		print "I am specific request"

class Adapter(Target):
	def __init__(self):
		self.a = Adaptee()

	def request(self):
		self.a.specific_request()

if __name__ == '__main__':
	a = Adapter()
	a.request()