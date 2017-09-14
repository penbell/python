class AM:
	
	def __init__(self, arg1, arg2):
		self.arg1 = arg1
		self.arg2 = arg2

	def adder(self):
		return self.arg1 + self.arg2

	def minus(self):
		return self.arg1 - self.arg2


arg1, arg2 = int(input('첫번째 수 ')), int(input('두번째 수'))

