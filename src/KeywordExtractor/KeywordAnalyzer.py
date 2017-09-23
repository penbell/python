from collections import Counter

class KeywordAnalyzer() :
    _tf = [] # tf값을 저장할 리스트.
    _df = {} # df값을 저장할 딕셔너리.
    _tfidf = [] # tfidf값을 저장할 리스트.

    def run(self, list1, keyword = None) : # 모든 함수를 실행 시키는 함수.
        self.tf_calc(list1)
        self.idf_calc()
        self.tfidf_calc()

        return self._tfidf

    def tf_calc(self, keyword) : # tf를 구해주는 함수.
        for i in range(len(keyword)) : # 여러 기사를 모두 처리할 만큼을 반복함.
            self._tf += [ Counter(keyword[i]) ] # 1개의 기사에서 tf값을 구하고 _tf에 dic를 리스트로 저장.

    def idf_calc(self) : # 실제로 df를 구해주는 함수.
        isolate = Counter() # 중복된 단어를 제거하기 위한 임시 변수

        for i in range(len(self._tf)): #_tf에 있는 모든 단어를 중복단어 제거.
            isolate += self._tf[i]

        for key in isolate.keys() : #df를 구하는 반복문

            for i in range(len(self._tf)): # tf길이 만큼 돌린다.

                if key in self._tf[i]: # isolate.keys()가 _tf[i]에 들어있으면 if 실행.
                                        # 즉, 단어가 n기사에 들어 있으면 카운팅 해주는 것.
                    if key in self._df : #값이 _df 이미 저장되어있으면 1을 누적.
                        self._df[key] += 1

                    else : # key를 처음 카운팅 해준다면 1값을 넣어준다.
                        self._df[key] = 1

    def tfidf_calc(self) : 
        for i in range(len(self._tf)) : # _tf 의 길이만큼 반복
            each = {}  # 임시로 딕셔너리 받을 위치 생성 
            
            for j in self._tf[i].keys() : # key값을 이용하여 tf*idf 계산
                each[j] = self._tf[i][j] / self._df[j] 
            
            self._tfidf += [ each ] # 넣어주기 ㅎ