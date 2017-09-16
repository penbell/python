class Mul_Div() :

    def _multiful(self, num1, num2) :
            return num1 * num2

    def _division(self, num1, num2) :
        try :
            return num1 / num2

        except Exception as e :
            print(e)
            return 0