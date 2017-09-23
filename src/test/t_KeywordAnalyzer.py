'''
@author : suhyun 이병욱
@data : 2017-09-19
@version : 1.4.0

@brief : check tf idf 
- python version : 3.5.x
- check tf idf tfidf run 
'''
from collections import Counter
import KeywordAnalyzer as testCode

dec1 = ['안녕','하세요']
dec2 = ['1,10,-1,10,3.4,-10.2','안녕','하세요','안녕']
dec3 = ['suhyun','안녕','안녕','안녕']
dec4 = ['안녕','하세요','반갑습니다.']
input1 = [dec2,dec3,dec4]
input2 = [dec1,dec3,dec4]
input3 = [dec1,dec2,dec4]
input4 = [dec1,dec2,dec3]
keyword = []
tfResult1 = [Counter({'안녕': 2, '1,10,-1,10,3.4,-10.2': 1, '하세요': 1}), Counter({'안녕': 3, 'suhyun': 1}), Counter({'안녕': 1, '하세요': 1, '반갑습니다.': 1})]
tfResult2 = [Counter({'안녕': 2, '1,10,-1,10,3.4,-10.2': 1, '하세요': 1}), Counter({'안녕': 3, 'suhyun': 1}), Counter({'안녕': 1, '하세요': 1, '반갑습니다.': 1}), Counter({'안녕': 1, '하세요': 1}), Counter({'안녕': 3, 'suhyun': 1}), Counter({'안녕': 1, '하세요': 1, '반갑습니다.': 1})]
tfResult3 = [Counter({'안녕': 2, '1,10,-1,10,3.4,-10.2': 1, '하세요': 1}), Counter({'안녕': 3, 'suhyun': 1}), Counter({'안녕': 1, '하세요': 1, '반갑습니다.': 1}), Counter({'안녕': 1, '하세요': 1}), Counter({'안녕': 3, 'suhyun': 1}), Counter({'안녕': 1, '하세요': 1, '반갑습니다.': 1}), Counter({'안녕': 1, '하세요': 1}), Counter({'안녕': 2, '1,10,-1,10,3.4,-10.2': 1, '하세요': 1}), Counter({'안녕': 1, '하세요': 1, '반갑습니다.': 1})]
tfResult4 = [Counter({'안녕': 2, '1,10,-1,10,3.4,-10.2': 1, '하세요': 1}), Counter({'안녕': 3, 'suhyun': 1}), Counter({'안녕': 1, '하세요': 1, '반갑습니다.': 1}), Counter({'안녕': 1, '하세요': 1}), Counter({'안녕': 3, 'suhyun': 1}), Counter({'안녕': 1, '하세요': 1, '반갑습니다.': 1}), Counter({'안녕': 1, '하세요': 1}), Counter({'안녕': 2, '1,10,-1,10,3.4,-10.2': 1, '하세요': 1}), Counter({'안녕': 1, '하세요': 1, '반갑습니다.': 1}), Counter({'안녕': 1, '하세요': 1}), Counter({'안녕': 2, '1,10,-1,10,3.4,-10.2': 1, '하세요': 1}), Counter({'안녕': 3, 'suhyun': 1})]
dfresult1 = {'1,10,-1,10,3.4,-10.2': 1, '안녕': 3, '하세요': 2, 'suhyun': 1, '반갑습니다.': 1}  
keywordtfidf = [{'1,10,-1,10,3.4,-10.2': 1.0, '안녕': 0.6666666666666666, '하세요': 0.5}, {'suhyun': 1.0, '안녕': 1.0}, {'안녕': 0.3333333333333333, '하세요': 0.5, '반갑습니다.': 1.0}]
runtest = [{'1,10,-1,10,3.4,-10.2': 1.0, '안녕': 0.6666666666666666, '하세요': 0.5}, {'suhyun': 1.0, '안녕': 1.0}, {'안녕': 0.3333333333333333, '하세요': 0.5, '반갑습니다.': 1.0}, {'1,10,-1,10,3.4,-10.2': 0.3333333333333333, '안녕': 0.2222222222222222, '하세요': 0.16666666666666666}, {'suhyun': 0.3333333333333333, '안녕': 0.3333333333333333}, {'안녕': 0.1111111111111111, '하세요': 0.16666666666666666, '반갑습니다.': 0.3333333333333333}, {'1,10,-1,10,3.4,-10.2': 0.3333333333333333, '안녕': 0.2222222222222222, '하세요': 0.16666666666666666}, {'suhyun': 0.3333333333333333, '안녕': 0.3333333333333333}, {'안녕': 0.1111111111111111, '하세요': 0.16666666666666666, '반갑습니다.': 0.3333333333333333}, {'안녕': 0.3333333333333333, '하세요': 0.5}, {'suhyun': 1.0, '안녕': 1.0}, {'안녕': 0.3333333333333333, '하세요': 0.5, '반갑습니다.': 1.0}, {'안녕': 0.3333333333333333, '하세요': 0.3333333333333333}, {'1,10,-1,10,3.4,-10.2': 1.0, '안녕': 0.6666666666666666, '하세요': 0.3333333333333333}, {'안녕': 0.3333333333333333, '하세요': 0.3333333333333333, '반갑습니다.': 1.0}, {'안녕': 0.3333333333333333, '하세요': 0.5}, {'1,10,-1,10,3.4,-10.2': 1.0, '안녕': 0.6666666666666666, '하세요': 0.5}, {'suhyun': 1.0, '안녕': 1.0}]

test = testCode.KeywordAnalyzer()

class testC:
	def testtf():
		#test와 맞는지 체크 
		if test.tf_calc(input1) == tfResult1 or test.tf_calc(input2) == tfResult2 or test.tf_calc(input3) == tfResult3 or test.tf_calc(input4) == tfResult4:
			print("tf test : true")
			return True
		else:
			print("tf test : False")
			return False

	def testidf():
		if test.idf_calc() == dfresult1:
			print("df test : true")
			return True
		else:
			print("df test : False")
			return False

	def testtfidf():
		test.tfidf_calc(keyword)
		if keywordtfidf == keyword:
			print("tfidf test : true")
			return True
		else:
			print("tfidf test : False")
			return False
	

	def testrun():
		test.run(input1,keyword)
		test.run(input2,keyword)
		test.run(input3,keyword)
		test.run(input4,keyword)
		if runtest == keyword:
			print("tfidf test : true")
			return True
		else:
			print("tfidf test : False")
			return False


if testC.testtf() and testC.testidf() and testC.testtfidf() and testC.testrun():
	print("all test good")
else:
	print("all test false")
