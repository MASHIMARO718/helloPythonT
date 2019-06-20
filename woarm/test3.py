
import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import re,urllib.request
from urllib.request import urlopen

class Pagessss:

    def __init__(self, opendate, ay,yg,bg,ajh,cz):
        self.opendate = opendate
        self.ay = ay
        self.yg = yg
        self.bg = bg
        self.ajh = ajh
        self.cz = cz

    def speak(self):
        print("开庭日期%s " %(self.opendate))
        print("案由%s" %(self.ay))
        print("原告%s" %(self.yg))
        print("被告%s" %(self.bg))
        print("案件号%s" %(self.ajh))
        print("操作%s" %(self.cz))


""" 你的 APPID AK SK """
# APP_ID = ''
# API_KEY = ''
# SECRET_KEY = ''
#
# client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
#
# """ 读取图片 """
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()
serachUrl = requests.get('http://localhost:34000/develop/companyurl/百度')
rss = serachUrl.content.decode('utf-8')
jss = json.loads(rss)
uur = jss['data']['redirectUrl']
# browser = webdriver.Chrome()
# browser.get("")
session = requests.Session()
r = session.get(uur)
r2 = session.get('')
s1 = BeautifulSoup(r2.text, 'html.parser')      # 使用bs4解析HTML对象
# token = s1.find('div', attrs={'id': '_container_announcementcourt'})
trs = s1.find_all('tr')
ss = set();
for tr in trs:
    ll = tr.find_all('td')
    if len(ll) >0:
        pages = Pagessss(ll[0].get_text(),ll[1].get_text(), ll[2].get_text(), ll[3].get_text(), ll[4].get_text(), ll[5].get_text())
        ss.add(pages)
    # for td in tr.find_all('td'):
    #     #     print(td.get_text())
for gg in ss:
    print(gg.ay)


#input_first = browser.find_elements(By.CLASS_NAME,"form-control")

#获取验证码
# urllib.request.urlretrieve('','F:\maven\\1.jpg')
# image = get_file_content('1.jpg')
# j = client.basicGeneral(image)
# codes = j['words_result'][0]['words']
#设置账户
# input_first[0].send_keys("")
# input_first[1].send_keys("")

# bu.click()
# browser.close()