# - *- coding: utf- 8 - *-
'''
@author : 조수현, 김윤희
@date : 2017. 9. 26
@version : 2.0.0

@brief : 기능1
- 파라미터 - scd:파일명, slist:문장, pos:명사목록, path:jvm.dll경로
             keyword:키워드,tfidf목록, id_m:키워드,채번 목록, iid_m:채번,키워드 목록
             index:키워드가 속한 문서들 목록
'''
from konlpy.tag import Twitter
from konlpy.utils import pprint

class SentenceManager() :
<<<<<<< HEAD
    
    def run(self, pos) :                                #문장 처리 수행
=======
    _count = 0

    def run(self, pos) :
>>>>>>> suhyun
        path = "C:/Program Files/Java/jdk1.7.0_55/jre/bin/server/jvm.dll"
        slist = []
        try :
            self.scd_parser('DOC1.SCD', slist)    # scd에서 문장 추출, #id, date는 별도 저장
<<<<<<< HEAD
            self.pos_tagger(slist[0:10000], pos, path)    # 문장 형태소 분석하여 명사 추출
=======
            self.pos_tagger(slist[0:10], pos, path)    # 문장 형태소 분석하여 명사 추출
>>>>>>> suhyun
            
            return 1
        except :
            return 0
            
<<<<<<< HEAD

=======
>>>>>>> suhyun
    def scd_parser(self, scd, slist) :
        sentence = open(scd,'r')
        try:
            for i in sentence :
                if i.startswith('<Contents>') :
<<<<<<< HEAD
                    slist.append(i[9:])
                    # slist.append(i.replace('<Contents>',''))
=======
                    slist.append(i.replace('<Contents>',''))
>>>>>>> suhyun
            return 1
        except Exception as ex :
            print(ex)
            return 0

    def pos_tagger(self, slist, pos, path) :
        twitter = Twitter(path)
<<<<<<< HEAD

        try:
            for one in slist :
=======
        try:
            # slist의 기사가 1개인경우 type이 str임으로 별도처리
            if type(slist) == str:
                print(slist)
                pos.append(twitter.nouns(slist))
                return 1

            print("len(slist) : ",len(slist))
            for one in slist :
                print(one)
>>>>>>> suhyun
                pos.append(twitter.nouns(one))
            return 1
        except Exception as ex :
            print(ex)
            return 0

<<<<<<< HEAD
    # def id_manager(self) :
    #     return

    # def indexer(self) :
=======

    def id_manager(self, keyword, id_m, iid_m) :
        for i in range(len(keyword)):
            for j in range(len(keyword[i])):
                key = keyword[i][j][0]
                if key in id_m:
                    continue
                
                id_m[key] = self._count
                iid_m[self._count] = key

                self._count += 1

    def indexer(self, keyword, index) :
        for i in range(len(keyword)):
            for j in range(len(keyword[i])):
                key = keyword[i][j][0]

                if key in index:
                    index[key] += [i]
                    continue
                
                index[key] = [i]
>>>>>>> suhyun
