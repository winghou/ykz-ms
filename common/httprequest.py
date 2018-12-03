import requests
from readconfig import Readconfig

class Http_request():
    def __init__(self,base_session,base_option,paramsfile_name,params_session,basefile_name="基本参数.ini"):
        base_cf = Readconfig(basefile_name)
        domain = base_cf.get_value('domain', 'domain')
        path = base_cf.get_value(base_session, base_option)
        self.url = domain + path
        params_cf = Readconfig(paramsfile_name)
        self.params = params_cf.get_item(params_session)

    def get(self):
        headers = {
            'Cookie': 'PHPSESSID=mq67huk8p72904v0qfgooffio6; Hm_lvt_af18264463096cae7c8902e3700efa59=1542806272,1543243138; Hm_lpvt_af18264463096cae7c8902e3700efa59=1543247831'
        }
        res = requests.get(self.url,params = self.params,headers = headers)
        # print(title)
        return res


if __name__ == '__main__':
    http = Http_request('path','query',"产品管理.ini","产品列表")
    http.get()




