 # -*- coding: utf-8 -*-

import bs4
import requests
import xlwt
import datetime
      
date = datetime.datetime.now().strftime('%Y-%m-%d')                    # 给文件打上时间戳，便于数据更新
url = 'http://127.0.0.1/wholesale.html'      # 网址
payload = {'SearchText': 'nike', 'page': '1', 'ie': 'utf8', 'g': 'y'}  # 字典传递url参数

# 初始化数据容器
title = []
price = []
order = []
store = []
      
# 爬取网页上的数据
for i in range(0, 5):        # 循环5次，就是5个页的商品数据
        payload['page'] = i+ 1    # 此处为页码，根据网页参数具体设置
        resp = requests.get(url, params=payload)
        soup = bs4.BeautifulSoup(resp.text, "html.parser")
        print(resp.url)          # 打印访问的网址
        resp.encoding = 'utf-8'  # 设置编码

        # 标题
        all_title = soup.find_all('a', class_='item-title')
        for j in all_title:
            soup_title = bs4.BeautifulSoup(str(j), "html.parser",)
            title.append(soup_title.a.string)

        # 价格
        all_price = soup.find_all('span', class_="price-current")
        for k in all_price:
            soup_price = bs4.BeautifulSoup(str(k), "html.parser")
            price.append(soup_price.span.string)
        # 订单量
        all_order = soup.find_all('a', class_="sale-value-link")
        for l in all_order:
            soup_order = bs4.BeautifulSoup(str(l), "html.parser")
            order.append(soup_order.a.string)
        # 店铺名称
        all_store = soup.find_all('a', class_="store-name")
        for m in all_store:
            soup_store = bs4.BeautifulSoup(str(m), "html.parser")
            store.append(soup_store.a.string)

# 数据验证
print(len(title))
print(len(price))
print(len(order))
print(len(store))
      
if len(title) == len(price) == len(order) == len(store):
    print("数据完整，生成 %d 组商品数据！" % len(title))
      
# 写入excel文档
print("正在写入excel表格...")
wookbook = xlwt.Workbook(encoding='utf-8')  # 创建工作簿
data_sheet = wookbook.add_sheet('demo')     # 创建sheet
      
# 生成每一行数据
for n in range(len(title)):
    data_sheet.write(n, 0, n+1)
    data_sheet.write(n, 1, title[n])        # n 表示行， 1 表示列
    data_sheet.write(n, 2, price[n])
    data_sheet.write(n, 3, order[n])
    data_sheet.write(n, 4, store[n])
      
      
wookbook.save("%s-%s.xls" % (payload['SearchText'], date))  #保存文件
print("写入excel表格成功！")