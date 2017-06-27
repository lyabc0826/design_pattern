#coding:utf-8
class Subject(object):
	def __init__(self):
		self.ob_list = []
	def attatch(self, ob):
		self.ob_list.append(ob)
	def detach(self, ob):
		self.ob_list.remove(ob)
	def notify(self):
		for ob in self.ob_list:
			ob.update()
class ConcreteSubject(Subject):
	def __init__(self):
		super(ConcreteSubject, self).__init__()
		self.sub_state = ''

class Observer(object):
	def update(self):
		raise NotImplementedError

class ConcreteObserver(Observer):
	def __init__(self, sub, name):
		self.sub = sub
		self.name = name
		self.ob_state = ''

	def update(self):
		self.ob_state = self.sub.sub_state
		print 'ob {} state {}'.format(self.name, self.ob_state)

if __name__ == '__main__':
	s = ConcreteSubject()
	ob1 = ConcreteObserver(s, 'ob1')
	ob2 = ConcreteObserver(s, 'ob2')
	s.attatch(ob1)
	s.attatch(ob2)
	s.sub_state = 'haha'
	s.notify()



