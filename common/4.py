import requests
import sys
import webbrowser
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
codeurl = 'http://b.yunkezan.com/admin/public/captcha?&v=0.46558944171422123'
valcode = requests.get(codeurl)
f = open('valcode.jpg','wb')
f.write(valcode.content)
f.close()
code = input("请输入验证码：")

login_url = 'http://b.yunkezan.com/admin/public/loginEp'

data = {
    'captcha':code,
    'userName':'5270bcb7521109e23908e541d4dfe0c0b569fd7e2fc15e7740a0240b6ebfdf775c01b309bbeb96f234367e8d27f394e9c109d10f7fb95112503ebdb15523815cbaf61a89ec38aba1c137038672c8d496cf6d7d338b36f245bcd841ba5303db2dab525e3a03e4e28ee9cb9e8ba15bdf1e32a69ef2b9ce85953cb9bea30fb8329c',
    'userPassword':'a22bafb71604b5548445650aac2e73e5f3ee4ba04bc437b511601b727eded75d5c9bc5ba7de610dd7691801b11d37db84e398e60340e542c854ea6a219f3ee263a5ac05ba07c34ebe46e43c7ca14f96b9383a28f1f0a0e9616154a6b2ccb01e70f04d313c29925e4b1943ef362c7a3b4cb9641f7e913283260f32c638d29dc11',
    'WjE4bkpnL1I5OXNSS0MrcDR1ODNLdz09': 'TDlOVTlCM2xwWnhSQWtZbEMvZkdCQT09',
    'lsession': 1
        }
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
          }
s = requests.Session()
page = s.get(login_url)
token1 = page.cookies['PHPSESSID']
cookie1 = 'PHPSESSID='+token1
print(cookie1)
res = s.post(login_url,data=data,headers=headers)
# print(res.cookies)
# token = res.cookies['PHPSESSID']
# cookie = 'PHPSESSID='+token
# print(cookie)

# session.cookies = requests.utils.cookiejar_from_dict(page)
# cookie = requests.utils.dict_from_cookiejar(session.cookies)
# print(res.content.decode('utf-8'))
# res1 = session.get('http://b.yunkezan.com/admin/roomstyle/index?weChatId=421&productType=3&hotelId=652&name=&statusIs=1')
headers = {
    'Cookie': token1,
    'Referer': 'http://b.yunkezan.com/admin/public/loginEp',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
          }
res1 = s.get('http://b.yunkezan.com/admin/public/index',headers = headers)
print(res1.text)


# print(res1.content.decode('utf-8'))
# print(res1.cookies)

url = 'http://b.yunkezan.com/admin/roomstyle/index'
params = {'weChatId': '421',
          'productType': '3',
          'hotelId': '652',
          'name': '',
          'statusIs': '1'
          }
headers = {
    'Cookie':cookie1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}
res2 = requests.get(url, params=params, headers=headers, verify=False)
# print(res2.content.decode('utf-8'))



