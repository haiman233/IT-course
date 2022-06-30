 # -*- coding: utf-8 -*-

import bs4
import requests
import xlwt
import datetime
      
date = datetime.datetime.now().strftime('%Y-%m-%d')                    # 给文件打上时间戳，便于数据更新
url = 'https://re.taobao.com/search?keyword=%E8%BF%9B%E5%8F%A3%E9%9B%B6%E9%A3%9F&catid=50010550&refpid=619362_1007&_input_charset=utf8&clk1=b93e1915c335dd925dfcbf24ae696b12&spm=a21bo.2017.201874-p4p.7.5af911d9f5vIK4'      # 网址
payload = {'SearchText': 'taob', 'page': '1', 'ie': 'utf8', 'g': 'y'}  # 字典传递url参数

# 初始化数据容器
title = []
store = []
price = []
paynum = []

# 爬取网页上的数据
for i in range(0, 5):        # 循环5次，就是5个页面的商品数据
        payload['page'] = i    # 此处为页码，根据网页参数具体设置
        resp = requests.get(url, params=payload)
        soup = bs4.BeautifulSoup(resp.text, "html.parser")
        print(resp.url)          # 打印访问的网址
        resp.encoding = 'utf-8'  # 设置编码

        # 标题
        all_title = soup.find_all('span', class_="title")
        for j in all_title:
            soup_title = bs4.BeautifulSoup(str(j), "html.parser", )
            title.append(soup_title.span.string)

        # 店铺名称
        all_store = soup.find_all('span', class_="shopNick")
        for k in all_store:
            soup_store = bs4.BeautifulSoup(str(k), "html.parser", )
            store.append(soup_store.span.string)

        # 价格
        all_price = soup.find_all('span', class_="pricedetail")
        for l in all_price:
            soup_price = bs4.BeautifulSoup(str(l), "html.parser")
            price.append(soup_price.strong.string)

        # 销售量
        all_paynum = soup.find_all('span', class_="payNum")
        for m in all_paynum:
            soup_paynum = bs4.BeautifulSoup(str(m), "html.parser")
            paynum.append(soup_paynum.span.string)

# 数据验证
print(len(title))
print(len(store))
print(len(price))
print(len(paynum))

if len(title) == len(store) == len(price) == len(paynum):
    print("数据完整，生成 %d 组商品数据！" % len(title))

# 写入excel文档
print("正在写入excel表格...")
wookbook = xlwt.Workbook(encoding='utf-8')  # 创建工作簿
data_sheet = wookbook.add_sheet('demo')     # 创建sheet
# 生成每一行数据
for n in range(len(title)):
    data_sheet.write(n, 0, n+1)
    data_sheet.write(n, 1, title[n])        # n 表示行， 1 表示列
    data_sheet.write(n, 2, store[n])
    data_sheet.write(n, 3, price[n])
    data_sheet.write(n, 4, paynum[n][:-3])
wookbook.save("taobao.xls")  #保存文件
print("写入excel表格成功！")
