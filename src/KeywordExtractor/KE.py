# @author : 허재혁
# @date : 2017. 9.
# @version : 3.5.2
#
# @brief :


import SentenceManager as sm
import KeywordAnalyzer as ka

class Keyword_Ext :

    def __init__(self):
        self.sm = sm.SentenceManager()
        self.ka = ka.KeywordAnalyzer()
        self.pos = []
        self.keyword = []
        self.r_keyword = []
        # self.id = {}
        # self.iid = {}
        # self.index = {}


    def run(self):
        sm.ret = self.sm.run(self.pos)
        if sm.ret == 1 :
            print("SM complete")
        else :
            print("SM error")
        ka.ret = self.ka.run(self.pos,self.keyword)
        if ka.ret == 1 :
            print("KA complete")
        else :
            print("KA error")

    # def temp(self):
    #     sm.id_manager(keyword,id,iid)
    #     sm.indexer(keyword,index)
    #     ka.relational_keyword_analyzer(keyword,r_keyword)


if __name__ == "__main__" :
    ke = Keyword_Ext()
    ke.run()


