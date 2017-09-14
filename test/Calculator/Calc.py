class Calc() :
    # def init(self, num1, num2) :
    #     self.num1 = num1
    #     self.num2 = num2

    def _multiful(self, num1, num2) :
        return num1 * num2

    def _division(self, num1, num2) :
        try :
            return num1 / num2
        except Exception as e:
            print('ValueError')
            return 0