import Calc 
import am

class Calculator() :
	def __init__(self):
		self.a = Calc.Calc()
		self.b = am.AM()
		self.run()

	def run(self) :
		print(self.a._multiful(4,2))
		print(self.a._division(4,2))
		print(self.b.adder(4,2))
		print(self.b.minus(4,2))

if __name__ == '__main__' :
	p = Calculator()

