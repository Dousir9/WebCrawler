import threading
import time
import requests
from queue import Queue
from bs4 import BeautifulSoup
import randomheader
import json
import datetime

pageQueue = Queue(maxsize=5)#与线程数相等的数
hrefQueue = Queue(maxsize=5)#线程数

global n, content
n = 0
content = []

#计算时间
def gettimediff(start, end):
    seconds = (end - start).seconds
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    diff = ("%02d:%02d:%02d" % (h, m, s))
    return diff

#持续将网页的页数入队列
class Find_Href(threading.Thread):
    def __init__(self, pagenum):
        super().__init__()
        self.pagenum = pagenum
        self.p = 1

    def run(self):
        while self.p <= self.pagenum:
            try:
                pageQueue.put(self.p)
                print("第{:.0f}页入队列".format(self.p))
                self.p = self.p + 1
            except:
                break

#持续将存放网页页数的队列弹出页数，对每一页处理
class Href_Put(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            if not pageQueue.empty():
                page = pageQueue.get()
                pageQueue.task_done()
                url = 'https://qd.anjuke.com/sale/jimoshi/p{}/#filtersort'.format(page)
                header = {
                    'User-Agent': randomheader.get_header()
                }
                try:
                    web_data = requests.get(url, headers=header, timeout=2)
                except:
                    print("连接失败1，将重新连接")
                    pageQueue.put(page)
                    continue
                soup = BeautifulSoup(web_data.content, 'lxml')
                links = soup.select('#houselist-mod-new > li > div.house-details > div.house-title > a')
                print(len(links))
                for link in links:
                    href = link.get("href")
                    self.get_info(href)
            else:
                break

    def get_info(self, href):
        global n, content
        time.sleep(0.1)
        header = {
            'User-Agent': randomheader.get_header()
        }
        href_data = requests.get(href, headers=header, timeout=5)
        if href_data.status_code == 200:
            soup = BeautifulSoup(href_data.content, 'lxml')
            addresses = soup.select(
                '#content > div.wrapper > div.wrapper-lf > div.houseInfoBox > div > div.houseInfo-wrap > ul > li:nth-child(4) > div.houseInfo-content > p > a:nth-child(2)')
            prices = soup.select(
                '#content > div.wrapper > div.wrapper-lf > div.clearfix > div.basic-info.clearfix > span.light.info-tag > em')
            areas = soup.select(
                '#content > div.wrapper > div.wrapper-lf > div.houseInfoBox > div > div.houseInfo-wrap > ul > li:nth-child(5) > div.houseInfo-content')
            unit_prices = soup.select(
                '#content > div.wrapper > div.wrapper-lf > div.houseInfoBox > div > div.houseInfo-wrap > ul > li:nth-child(3) > div.houseInfo-content')
            for address, price, area, unit_price in zip(addresses, prices, areas, unit_prices):
                data = {
                    '地址': address.get_text().strip(),
                    '总价': price.get_text().strip() + '万元',
                    '平米单价': unit_price.get_text().strip(),
                    '大小': area.get_text().strip(),
                }
                content.append(data)
                n = n+1
                print(data)
        else:
            print("连接失败2")
            self.get_info(href)


if __name__ == '__main__':
    find_href_thred = Find_Href(50)#爬取的页数
    find_href_thred.start()
    t1 = []
    start = datetime.datetime.now()  # 开始时间
    for i in range(5):#线程数
        put_href_thread = Href_Put()
        put_href_thread.start()
        t1.append(put_href_thread)
    for t in t1:
        t.join()
        print("挂了")
    end = datetime.datetime.now()  # 结束时间
    diff = gettimediff(start, end)  # 计算耗时
    print('一共爬取信息: %s 条,共耗时: %s \n' % (n, diff))
    with open('即墨市.json', 'w') as fp:  # 将所得的数据存储为json文件
        fp.write(json.dumps(content, indent=2, ensure_ascii=False))