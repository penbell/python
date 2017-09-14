import Calc
import am

class Calculator() :
	def __init__(self):
		self.a = Calc.Calc()
		self.b = am.AM()
		self.run()

	def run(self) :
		self.a.multful()
		self.a.division()
		self.b.adder()
		self.b.minus()

if __name__ == '__main__' :
	p = Calculator()

