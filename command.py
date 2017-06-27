class Command(object):
	def __init__(self, r):
		self.reveiver = r
	def execute(self):
		raise NotImplementedError

class ConcreteCommand(Command):
	def execute(self):
		self.reveiver.action()

class Invoker(object):
	def __init__(self):
		self.comm = None
	def set_comm(self, c):
		self.comm = c
	def execute_commm(self):
		self.comm.execute()
class Receiver(object):
	def action(self):
		print 'execute process'

if __name__ == '__main__':
	r = Receiver()
	c = ConcreteCommand(r)
	i = Invoker()
	i.set_comm(c)
	i.execute_commm()
