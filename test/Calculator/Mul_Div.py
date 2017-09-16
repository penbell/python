'''
@author : 이병욱 suhyun
@data : 2017-09-16
@version : 1.0.0

@brief : check multiful and division
- python version : 3.5.x
'''
class Mul_Div() :

    def _multiful(self, num1, num2) :
            return num1 * num2

    def _division(self, num1, num2) :
        try :
            return num1 / num2
        except Exception as e :
            print(e)
            return 0