import calc
import am

class Calculator() :
	def __init__(self):
		self.a = calc.Calc()
		self.b = am.AM()
		self.run()

	def run(self) :
		self.a.test()
		self.b.test()

if __name__ == '__main__' :
	p = Calculator()

