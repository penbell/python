'''
@author: 신승식, 김윤희
@date: 2017.9.19
@version: 1.0.1

@brief: sentence manager
-python version:3.5.2
-Use class: SentenceManager
-test parameter: arg1, arg2
'''
import time
import SentenceManager

# 클래스 호출
p = SentenceManager.SentenceManager()
pos = []

start = time.time()
print(p.run(pos))

end = time.time() - start
print(" end: [" + str(round(end,2)) + " sec]")
