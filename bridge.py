class Implementor(object):
	def operation(self):
		raise NotImplementedError

class ConcreteImplementorA(Implementor):
	def operation(self):
		print "A"

class ConcreteImplementorB(Implementor):
	def operation(self):
		print "B"

class Abstraction(object):
	def __init__(self):
		self.impl = None
	def set_impl(self, impl):
		self.impl = impl
	def operation(self):
		raise NotImplementedError

class RefineAbstraction(Abstraction):
	def operation(self):
		self.impl.operation()

if __name__ == '__main__':
	r = RefineAbstraction()
	a = ConcreteImplementorA()
	r.set_impl(a)
	r.operation()
	b = ConcreteImplementorB()
	r.set_impl(b)
	r.operation()