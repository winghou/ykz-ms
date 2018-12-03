# import requests
# import webbrowser
# webbrowser.open('http://b.yunkezan.com/admin/roomstyle/index')


import time
import requests
from selenium import webdriver
import json

# driver = webdriver.Chrome() #
# driver.get('http://b.yunkezan.com/admin/public/loginEp');#进入这个登陆网站
# element =  driver.find_element_by_id("loginform_user")#获取账号栏的标签
# element.send_keys("mashan")#给账号栏里输出账号
# element =  driver.find_element_by_id("loginform_capt")
# element =  driver.find_element_by_id("loginform_pass")
# element.send_keys("shan285840@")# 输入密码
# verif = input("请输入验证码：")
# print(verif)
# element =  driver.find_element_by_id("loginform_capt")
# element.send_keys(verif)
# element = driver.find_element_by_class_name("subbtn").click() #点击下面的登陆按钮
#
# time.sleep(2)

# driver.get(url)
# r = requests.get(url)
# print(r.content)

def get_session(url,data,headers):
    session = requests.Session()
    session.post(url,data=data,headers=headers)
    return session
# url = 'http://b.yunkezan.com/admin/roomstyle/index?weChatId=421&productType=3&hotelId=652&name=&statusIs=1'
url = 'http://b.yunkezan.com/admin/public/loginEp'
data = {
    'captcha':'byiy',
    'userName':'2de66a5f7869d581266a26ecfdbffc687be705d8a7442ce12decf8d0005630b1ed95555785b90c733e22751f30a6530f3185f606f99a9beb436884659f430ddd233e9e5e9e24883cffd174fef29da5f99cc2d3e4165b4128b49f3b885902777deb1e3ffa12516e4d8284805c735ea2356ea42d73e61f2e9b87c09c1b005f4351',
    'userPassword':'2618e3b3f40a8cb339b9e38a7ed6384c36197fda003467ed5e47e9a7a972b0ad6edb13743376727068388e4cde9ef8f5adca027e01d0ebfff4f26a2a955896051c4de0d92e800b9fd9589a11ff2bb8506ff293e5f7734457619f59fca93eb6b5927acbfb5c4459fdce9f4944d088bc35a298ef3fc5f8e7e41224b48b92c256eb',
    'T2c4Q0hwMmY3SUx3RXR6U3FOTnZsdz09':'b05BUytQMWxIMEM0QUZQVGVyRUFrUT09'
}
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}
session = get_session(url,data,headers)
res = session.get('http://b.yunkezan.com/admin/roomstyle/index?weChatId=421&productType=3&hotelId=652&name=&statusIs=1')
print(res.text)

# url = 'http://b.yunkezan.com/admin/roomstyle/index?weChatId=421&productType=3&hotelId=652&name=&statusIs=1'
# params = {'weChatid':'373',
#           'productType':'3',
#           'hotel':'410',
#           'name':'',
#           'statusls':'1'
#          }
# # res = requests.get(url,params=params,verify=False)
# res = requests.get(url)
# print(res.text)
#
# 会话对象requests.Session能够跨请求地保持某些参数，比如cookies，即在同一个Session实例发出的所有请求都保持同一个cookies,
# 而requests模块每次会自动处理cookies，这样就很方便地处理登录时的cookies问题。