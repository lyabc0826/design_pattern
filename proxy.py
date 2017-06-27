#coding:utf-8

class Subject(object):
	def request(self):
		raise NotImplementedError

class RealSubject(Subject):
	def request(self):
		print "I am realsubject"

class Proxy(Subject):
	def __init__(self):
		self.real = RealSubject()
	def request(self):
		self.real.request()

if __name__ == '__main__':
	p = Proxy()
	p.request()