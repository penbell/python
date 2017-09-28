'''
@author : suhyun 이병욱
@data : 2017-09-28
@version : 1.0.4

@brief : check tf, idf, tfidf, normalizer
- python version : 3.5.x
- check tf, idf, tfidf, normalizer
- variables
   - _tf : tf 계산된 값을 list안에 문서별로 counter된 값은 입력
   - _df : 중복된 단어를 제거하고 _df변수에 df값을 채워넣는다
   - each : tfidf가 계산된 dictionary
'''
import time
import operator
from collections import Counter #
import copy

class KeywordAnalyzer() :
    _tf = [] 
    _df = {}

    def run(self, list1, keyword) : # 모든 함수를 실행 시키는 함수.
        try :
            self.tf_calc(list1)
            self.idf_calc()
            self.tfidf_calc(keyword)
            self.reset()
            return 1 , 'ok'

        except Exception as ex:
            return 0, ex

    def tf_calc(self, list1) :
        # tf를 계산하는 함수.
        try :
            for i in range(len(list1)) :
                self._tf += [ Counter(list1[i]) ] # 1개의 기사에서 tf값을 구하고 _tf에 dic를 리스트로 저장.
        except Exception as ex:
            print(ex)
            return 0
    def idf_calc(self) :
        '''
        실제로 df를 계산하는 함수.
        중복된 단어를 제거하고 _df변수에 df값을 채워넣는다.
        '''
        try:
            isolate = Counter()

            for i in range(len(self._tf)):
                isolate += self._tf[i]

            for key in isolate.keys() :

                for i in range(len(self._tf)):

                    if key in self._tf[i]: #isolate.keys()가 _tf[i]에 들어있으면 if 실행.
                                            #즉, 단어가 n기사에 들어 있으면 카운팅 해주는 것.
                        if key in self._df :
                            self._df[key] += 1

                        else :
                            self._df[key] = 1
            return 1, "ok"
        except Exception as ex:
            return 0, ex
    def tfidf_calc(self,keyword) :
        '''
        tfidf를 계산하는 함수.
        임시로 딕셔너리 받을 위치 생성(한 문서를 돌때마다 새로 생성.) 하고
        keyword에 값을 넣는다.
        '''
        try:
            for i in range(len(self._tf)) :

                each = {}

                for j in self._tf[i].keys() :
                    each[j] = self._tf[i][j] / self._df[j]

                each = self.normalizer(each)
                keyword += [sorted(each.items(), key=operator.itemgetter(1), reverse=True)]
            return 1, "ok"
        except Exception as ex:
            print(ex)
            return 0, ex

    def reset(self) :
        self._tf = []

# func normalizer # tf-idf 점수 평준화(0~100점)
    def normalizer(self,k_dict):
        max_value = max(k_dict.values())

        for key in k_dict.keys():
             k_dict[key] = int((k_dict[key] / max_value) * 100)
        return k_dict




