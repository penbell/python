'''
@author : 김문종, 허재혁
@date : 2017. 9.
@version : 3.5.2

@brief : 키워드 추출 및 문장 처리 main class
- 파라미터 : pos(리스트), keyword(리스트), r_keyword(리스트)
- sm 클래스에 pos를 넘겨서 추출된 키워드를 넘겨받는다.
  sm 클래스에서 받은 pos와 비어있는 keyword 리스트를 ka 클래스에 넘긴다.
  ka 클래스에서 받은 pos와 sorting된 keyword 리스트를 출력.
'''

import time
import SentenceManager as sm
import KeywordAnalyzer as ka

class Keyword_Ext :

    def __init__(self):
        self.sm = sm.SentenceManager()
        self.ka = ka.KeywordAnalyzer()
        self.pos = []
        self.keyword = []
        self.r_keyword = []
        self.key_id = {}
        self.key_iid = {}
        self.index = {}

    def run(self):
        self.check(self.sm.run(self.pos), 'sm.run')
        self.check(self.ka.run(self.pos,self.keyword), 'ka.run')
        self.check(self.sm.id_manager(self.keyword, self.key_id, self.key_iid), 'id_manager')
        self.check(self.sm.id_indexer(self.keyword, self.index), 'indexer')

    def check(self, ret, ex, i) :
        if ret is 1 :
            print("{} is success!".format(i))
        elif ret is 0 :
            print("{} is fail! :[{}]".format(i, ex))

    def print_pos(self):
        print(self.pos)

    def print_keyword(self):
        print(self.keyword)

    def write_pos(self):
        f = open("pos_result.txt", "w")
        for sentence in self.pos:
            f.write("{}\n".format(str(sentence)))

    def write_keyword(self):
        f = open("keyword_result.txt","w")
        for sentence in self.keyword:
            f.write("{}\n".format(str(sentence)))

if __name__ == "__main__" :
    start = time.time()
   
    ke = Keyword_Ext()
    ke.run()
    
    end = time.time() - start
    print("complete: [" + str(round(end, 2)) + "second ]")

    #pos keyword 출력
    #ke.print_pos()
    #ke.print_keyword()

    # file write
    ke.write_pos()
    ke.write_keyword()