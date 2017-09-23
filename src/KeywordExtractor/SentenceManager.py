'''
@author : 신승식, 김윤희
@date : 2017. 9. 19
@version : 1.0.0

@brief : 기능1
- 파라미터 - scd:파일명, sentence:문장

'''
from konlpy.tag import Twitter
from konlpy.utils import pprint

class SentenceManager() :
    
    def run(self, pos) :                                #문장 처리 수행
        path = "C:/Program Files/Java/jdk1.7.0_55/jre/bin/server/jvm.dll"
        slist = []
        try :
            self.scd_parser('DOC1.SCD', slist)    # scd에서 문장 추출, #id, date는 별도 저장
            self.pos_tagger(slist[0:10000], pos, path)    # 문장 형태소 분석하여 명사 추출
            
            return 1
        except :
            return 0
            

    def scd_parser(self, scd, slist) :
        sentence = open(scd,'r')
        try:
            for i in sentence :
                if i.startswith('<Contents>') :
                    slist.append(i[9:])
                    # slist.append(i.replace('<Contents>',''))
            return 1
        except Exception as ex :
            print(ex)
            return 0

    def pos_tagger(self, slist, pos, path) :
        twitter = Twitter(path)

        try:
            for one in slist :
                pos.append(twitter.nouns(one))
            return 1
        except Exception as ex :
            print(ex)
            return 0

    # def id_manager(self) :
    #     return

    # def indexer(self) :