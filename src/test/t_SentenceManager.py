'''
@author: 신승식, 김윤희
@date: 2017.9.23
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
slist = []
path = "C:/Program Files/Java/jdk1.7.0_55/jre/bin/server/jvm.dll"
start = time.time()
# print(p.run(pos, slist))
try:
   print(p.scd_parser('DOC.SCD', slist))
except Exception as ex:
   print(ex)

try:
   print(p.pos_tagger('청와대 수석-보좌관 10명도 24일 재산을 신고했다. 이들의 평균재산은 12억8800만원이었다.', pos, path))
except Exception as ex:
   print(ex)

end = time.time() - start
print(" end: [" + str(round(end,2)) + " sec]")