import Calc as cal

X = [1,2,3,4,5,6,7,8,9,10,-1,-2,-3,-4,-5,-6,-7,"test"]
Y = [1,2,3,4,5,6,7,8,9,10,-1,-2,-3,-5,-7,10,"test"]

test = cal.Calc()
# print(test._multiful(1,2))

class CheckCal:
	def testMultiful():
		for x in X:
			for y in Y:
				if test._multiful(x,y) == x*y:
					print("x : ",x," y : ",y ,"result",x*y,"-->true")
				else:
					print("x : ",x," y : ",y ,"result",cal.test._multiful(x,y),"-->fail")

	def testDivision():
		for x in X:
			for y in Y:
				if test._division(x,y) == x/y:
					print("x : ",x," y : ",y ,"result",x*y,"-->true")
				else:
					print("x : ",x," y : ",y ,"result",test.divison(x,y),"-->fail")

				if test._division(x,0) == 0:
					print("x : ",x," y : 0  result-->true")
				else:
					print("x : ",x," y : 0  result -->false")


CheckCal.testMultiful()
CheckCal.testDivision()