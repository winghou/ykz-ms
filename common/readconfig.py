from rewconfigparser import Rewconfigparser
import os

prjdir = os.path.dirname(os.path.dirname(__file__))
cfdir = os.path.join(prjdir+'/config/')
# print(cfdir)

class Readconfig():
    def __init__(self,file_name):
        self.file_path = cfdir+file_name
        self.cf = Rewconfigparser()
        self.cf.read(self.file_path,"utf-8")

    def get_value(self,session,option):
        value = self.cf.get(session,option)  #返回session的list
        return value
    def get_item(self,session):
        value = self.cf.items(session)
        value = dict(value)
        return value




