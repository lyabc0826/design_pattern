#coding:utf-8
class Operation(object):
	def __init__(self):
		self.num_a = 0
		self.num_b = 0

	def operate(self):
		raise NotImplementedError

class OperationAdd(Operation):
	def __init__(self):
		super(OperationAdd, self).__init__()

	def operate(self):
		return self.num_a+self.num_b

class OperationMinus(Operation):
	def __init__(self):
		super(OperationAdd, self).__init__()

	def operate(self):
		return self.num_a-self.num_b

class OperationFactory(object):
	def operationCreate(self, op):
		if op == '+':
			o = OperationAdd()
		elif op == '-':
			o = OperationAdd()
		else:
			raise Exception("operate is not support")
		o.num_a = 2
		o.num_b = 1
		print o.operate()

if __name__ == '__main__':
	ins = OperationFactory()
	ins.operationCreate('+')
