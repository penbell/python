'''
@author : suhyun 이병욱
@data : 2017-09-19
@version : 1.0.2

@brief : check tf idf 
- python version : 3.5.x
- check tf idf tfidf
'''
from collections import Counter
import KeywordAnalyzer as key

dec1 = ['안녕','하세요']
dec2 = ['1,10,-1,10,3.4,-10.2','안녕','하세요','안녕']
dec3 = ['suhyun','안녕','안녕','안녕']
dec4 = ['안녕','하세요','반갑습니다.']
input1 = [dec2,dec3,dec4]
input2 = [dec1,dec3,dec4]
input3 = [dec1,dec2,dec4]
input4 = [dec1,dec2,dec3]
input5 = [dec1,dec2,dec3,dec4]



test = key.KeywordAnalyzer()

class testC:
	def testtf():
		print("tf 문서 1 : ",test.tf_calc(input1))
		print()
		print("tf 문서 2 : ",test.tf_calc(input2))
		print()
		print("tf 문서 3 : ",test.tf_calc(input3))
		print()
		print("tf 문서 4 : ",test.tf_calc(input4))
		print()
		print("전체보내기 : ",test.tf_calc(input5))

	def testidf():
		print()
		print("idf_calc() : ",test.idf_calc())
	
	def testrun():
		print("run 문서 1 : ",test.run(input1))
		print()
		print("run 문서 2 : ",test.run(input2))
		print()
		print("run 문서 3 : ",test.run(input3))
		print()
		print("run 문서 4 : ",test.run(input4))
		print()
		print("전체보내기 : ",test.run(input5))

# test2 = {'a':'3','b':4}
# test3 = Counter(['a','a','a','b','b','c'])

# if 'a' in test2:
# 	print("a있음")

# if 'a' in test3:
# 	print("a있음")

# testC.testtf()
# testC.testidf()
testC.testrun()
