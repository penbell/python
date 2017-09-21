'''
@author : suhyun 이병욱
@data : 2017-09-16
@version : 1.0.0

@brief : check multiful and division
- python version : 3.5.x
'''
import Mul_Div as cal

X = [1,2,3,4,5,6,7,8,9,10,-1,-2,-3,-4,-5,-6,-7]
Y = [1,2,3,4,5,6,7,8,9,10,-1,-2,-3,-5,-7,10]

test = cal.Mul_Div()
# print(test._multiful(1,2))

class CheckCal:
	def testMultiful():
		for x in X:
			for y in Y:
			# 	if type(x) == str or type(y) == str:
			# 		print("test._multiful({},{}) : ".format(x,y)+test._multiful(x,y))
				# else:
				if test._multiful(x,y) == x*y:
					print("_multiful x : ",x," y : ",y ,"result",test._multiful(x,y),"-->true")
				else:
					print("_multiful x : ",x," y : ",y ,"result",test._multiful(x,y),"-->fail")

	def testDivision():
		for x in X: 
			for y in Y:

				# if type(x) == str or type(y) == str:
				# 	print("test._multiful({},{}) : ".format(x,y)+test._multiful(x,y))
				# else:
				if test._division(x,y) == x/y:
					print("_division x : ",x," y : ",y ,"result",test._division(x,y),"-->true")
				else:
					print("_division x : ",x," y : ",y ,"result",test._division(x,y),"-->fail")

				if test._division(x,0) == 0:
					print("_division x : ",x," y : 0  result-->true")
				else:
					print("_division x : ",x," y : 0  result -->false")


CheckCal.testMultiful()
CheckCal.testDivision()