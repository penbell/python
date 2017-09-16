'''
@author : 김윤희
@date : 2017. 9. 16
@version : 1.0.0

@brief : 구구단 메인
- a, b : 입력 숫자
- f : 연산자
'''
import Mul_Div 
import am


class Calculator() :

    def __init__(self):
        self.a = Mul_Div.Mul_Div()
        self.b = am.PLUS_MINUS()

    def run(self, a, b, f) :
        if f == '+' :
            print(self.b.plus(a, b))
        elif f == '-' :
            print(self.b.minus(a, b))
        elif f == '*' :
            print(self.a._multiful(a, b))
        elif f == '/' :
            print(self.a._division(a, b))
        else :
            print('연산 기호가 이상합니다.')

    def isNumber(s):
        try:
            int(s)
            return True
        except ValueError:
            return False


if __name__ == '__main__' :

    while True:
        p = Calculator()
        a, b, f = input('계산할 두 수와 연산자를 입력해주세요 >').split()

        if p.isNumber(a) and p.isNumber(b) :
            p.run(int(a), int(b), f)
            break
        else :
            print('올바른 수가 아닙니다. 다시 입력 해주세요.')
            continue

