 # -*- coding: utf-8 -*-

import bs4
import requests
import csv

url = 'https://re.taobao.com/search?keyword=%E8%BF%9B%E5%8F%A3%E9%9B%B6%E9%A3%9F&catid=50010550&refpid=619362_1007&_input_charset=utf8&clk1=b93e1915c335dd925dfcbf24ae696b12&spm=a21bo.2017.201874-p4p.7.5af911d9f5vIK4'      # 网址
payload = {'SearchText': 'taob', 'page': '1', 'ie': 'utf8', 'g': 'y'}  # 字典传递url参数

# 初始化数据容器
price = []
paynum = []
comment= []

# 爬取网页上的数据
for i in range(0, 1):        # 循环1次，就是1个页面的商品数据
        payload['page'] = i    # 此处为页码，根据网页参数具体设置
        resp = requests.get(url, params=payload)
        soup = bs4.BeautifulSoup(resp.text, "html.parser")
        print(resp.url)          # 打印访问的网址
        resp.encoding = 'utf-8'  # 设置编码

        # 价格
        all_price = soup.find_all('span', class_="pricedetail")
        for k in all_price:
            soup_price = bs4.BeautifulSoup(str(k), "html.parser")
            price.append(soup_price.strong.string)
        # 销售量
        all_paynum = soup.find_all('span', class_="payNum")
        for l in all_paynum:
            soup_paynum = bs4.BeautifulSoup(str(l), "html.parser")
            paynum.append(soup_paynum.span.string)
        # 评价
        all_comment = soup.find_all('span', class_="dsr-info-num")
        for m in all_comment:
            soup_comment = bs4.BeautifulSoup(str(m), "html.parser")
            comment.append(soup_comment.span.string)

# 写入csv文档
datas=[['price','paynum','comment']]
for n in range(len(price)):
     data=[price[n],paynum[n][:-3],comment[n]]
     datas.append(data)
with open('data_sample.csv', 'w', newline='') as csvfile:
    writer  = csv.writer(csvfile)
    for row in datas:
        writer.writerow(row)
