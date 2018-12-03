import unittest
import sys
sys.path.append(r"E:\Python\ykz-ms\common")
import readconfig
from httprequest import Http_request
from lxml import html

class package(unittest.TestCase):
    # def __init__(self):
    #     super().__init__(self)
    def setUp(self):
        super().setUp()

    def test_query_package(self):
        http = Http_request('path', 'query', "产品管理.ini", "产品列表")
        res = http.get()
        etree = html.etree
        selector = etree.HTML(res.text)
        # print(selector)
        cont = selector.xpath('//tr/td/text()')  # 或者：  selector.xpath('//tr[descendant::td]/td/text()')
        # cont = ' '.join(cont).split()  # 此方法会导致“最新修改时间的日期和时间分成两个字段，不可取
        content = []
        for each in cont:
            each = each.strip()
            content.append(each)
        # while '' in content:
        #     content.remove('')
        content = list(filter(None, content))  # 去除列表中的空字符
        print(content)

        count = len(selector.xpath('//tr'))  # --获取列表数据总数
        # print(count)
        title = ['序号', 'id', '商品名称', '标题名称', '所属酒店', '售价', '库存', '审核状态', '最新修改时间', '状态'] * count
        print(title)
        # print(dict(zip(content,title)))

        title = selector.xpath('//*[@id="j-orderlist"]/tbody/tr[1]/comment()[2]')  # 获取标题
        print(title)
if __name__ == '__main__':
    package = package()
    package.test_query_package()


