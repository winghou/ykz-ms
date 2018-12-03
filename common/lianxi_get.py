import requests
from lxml import html
from readconfig import Readconfig


cfg = Readconfig("基本参数.ini")
domain = cfg.get_value("domain","domain")
# print(domain)

class Httprequest():

    def get(self,session,option):
        params = {'weChatId': '421',
                  'productType': '3',
                  'hotelId': '652',
                  'name': '',
                  'statusIs': '1'
                  }
        headers = {
            # 'Cookie': 'Hm_lvt_af18264463096cae7c8902e3700efa59=1542806398,1542892920; PHPSESSID=elpis1d3njljcd4o8bajjvf2q4'
            'Cookie': 'Hm_lvt_af18264463096cae7c8902e3700efa59=1542806272; PHPSESSID=mq67huk8p72904v0qfgooffio6'
        }
        path = cfg.get_value(session,option)
        url = domain+path
        res = requests.get(url, params=params, headers=headers, verify=False)
        etree = html.etree
        selector = etree.HTML(res.text)
        # print(selector)
        cont = selector.xpath('//tr/td/text()')   # 或者：  selector.xpath('//tr[descendant::td]/td/text()')
        # cont = ' '.join(cont).split()  # 此方法会导致“最新修改时间的日期和时间分成两个字段，不可取
        content = []
        for each in cont:
            each = each.strip()
            content.append(each)
        # while '' in content:
        #     content.remove('')
        content = list(filter(None,content)) #去除列表中的空字符
        print(content)

        count = len(selector.xpath('//tr'))  # --获取列表数据总数
        # print(count)
        title = ['序号', 'id', '商品名称', '标题名称', '所属酒店', '售价', '库存', '审核状态', '最新修改时间', '状态'] * count
        print(title)
        # print(dict(zip(content,title)))

        title = selector.xpath('//*[@id="j-orderlist"]/tbody/tr[1]/comment()[2]')  # 获取标题
        print(title)


        # print(cont.split())


if __name__ == '__main__':
    httpreq = Httprequest()
    httpreq.get('path','query')

