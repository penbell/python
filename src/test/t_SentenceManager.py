# - *- coding: utf- 8 - *-
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

id_m = {}
iid_m = {}
keyword = [[('1,10,-1,10,3.4,-10.2', 1.0), ('안녕', 0.6666666666666666), ('하세요', 0.5)], [('suhyun', 1.0), ('안녕', 1.0)], [('반갑습니다.', 1.0), ('하세요', 0.5), ('안녕', 0.3333333333333333)], [('하세요', 0.25), ('안녕', 0.16666666666666666)], [('suhyun', 0.5), ('안녕', 0.5)], [('반갑습니다.', 0.5), ('하세요', 0.25), ('안녕', 0.16666666666666666)], [('하세요', 0.14285714285714285), ('안녕', 0.1111111111111111)], [('1,10,-1,10,3.4,-10.2', 0.5), ('안녕', 0.2222222222222222), ('하세요', 0.14285714285714285)], [('반갑습니다.', 0.3333333333333333), ('하세요', 0.14285714285714285), ('안녕', 0.1111111111111111)], [('하세요', 0.1111111111111111), ('안녕', 0.08333333333333333)], [('1,10,-1,10,3.4,-10.2', 0.3333333333333333), ('안녕', 0.16666666666666666), ('하세요', 0.1111111111111111)], [('suhyun', 0.3333333333333333), ('안녕', 0.25)]]
index = {} # 키워드 별 문서 id indexing   

start = time.time()

# print(p.run(pos, slist))

try:
   print(p.scd_parser('DOC1.SCD', slist))
   # print(slist[0:2])
except Exception as ex:
   print(ex)

print("________________________________________")
print()

try:
   print(p.pos_tagger(slist[0:2], pos, path))
   print(pos)
except Exception as ex:
   print(ex)

# try:
#     p.id_manager(keyword, id_m, iid_m)
#     print(id_m)
#     print(iid_m)
# except Exception as ex:
#     print(ex)

# print("________________________________________")
# print()

# try:
#     p.indexer(keyword, index)
#     print(index)
# except Exception as ex:
#     print(ex)


end = time.time() - start
print(" end: [" + str(round(end,2)) + " sec]")