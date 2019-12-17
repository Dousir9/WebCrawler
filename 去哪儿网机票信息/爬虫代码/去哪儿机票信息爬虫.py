from urllib import parse
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import json
import threading
from queue import Queue
from bs4 import BeautifulSoup

dataQueue = Queue(maxsize=3)

global content
content = []

#持续将日期入队列
class Find_date(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        now = datetime.datetime.now()
        now_year = int(datetime.datetime.strftime(now, '%Y'))
        now_month = int(datetime.datetime.strftime(now, '%m'))
        now_day = int(datetime.datetime.strftime(now, '%d'))
        if now_month == 1 or now_month == 3 or now_month == 5 or now_month == 7 or now_month == 8 or now_month == 10 or now_month == 12:
            if now_day < 31:
                now_day += 1
            elif now_month != 12:
                now_month += 1
                now_day = 1
            else:
                now_year += 1
                now_month = 1
                now_day = 1
        elif now_month == 4 or now_month == 6 or now_month == 9 or now_month == 11:
            if now_day < 30:
                now_day += 1
            else:
                now_month += 1
                now_day = 1
        elif now_month == 2:
            if (now_year % 4 == 0 and now_year % 100 != 0) or now_year % 400 == 0:
                if now_day < 29:
                    now_day += 1
                else:
                    now_month += 1
                    now_day = 1
            else:
                if now_day < 28:
                    now_day += 1
                else:
                    now_month += 1
                    now_day = 1
        year = int(datetime.datetime.strftime(now, '%Y'))
        month = int(datetime.datetime.strftime(now, '%m'))
        day = int(datetime.datetime.strftime(now, '%d'))
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day < 31:
                day += 1
            elif month != 12:
                month += 1
                day = 1
            else:
                year += 1
                month = 1
                day = 1
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day < 30:
                day += 1
            else:
                month += 1
                day = 1
        elif now_month == 2:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                if day < 29:
                    day += 1
                else:
                    month += 1
                    day = 1
            else:
                if day < 28:
                    day += 1
                else:
                    month += 1
                    day = 1
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day < 12:
                day += 20
            elif month != 12:
                month += 1
                day = 20 - (31 - day)
            else:
                year += 1
                month = 1
                day = 20 - (31 - day)
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day < 11:
                day += 20
            else:
                month += 1
                day = 20 - (30 - day)
        else:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                if day < 10:
                    day += 20
                else:
                    month += 1
                    day = 20 - (29 - day)
            else:
                if day < 9:
                    day += 20
                else:
                    month += 1
                    day = 20 - (28 - day)
        while now_year < year or now_month < month or now_day < day:
            if now_month < 10:
                m = "0" + str(now_month)
            else:
                m = str(now_month)
            if now_day < 10:
                d = "0" + str(now_day)
            else:
                d = str(now_day)
            goDate = str(now_year) + "-" + m + "-" + d
            print(goDate)
            if now_month == 1 or now_month == 3 or now_month == 5 or now_month == 7 or now_month == 8 or now_month == 10 or now_month == 12:
                if now_month != 12:
                    if now_day == 31:
                        now_day = 1
                        now_month += 1
                    else:
                        now_day += 1
                else:
                    if now_day == 31:
                        now_day = 1
                        now_month = 1
                        now_year += 1
                    else:
                        now_day += 1
            elif now_month == 4 or now_month == 6 or now_month == 9 or now_month == 11:
                if now_day == 30:
                    now_day = 1
                    now_month += 1
                else:
                    now_day += 1
            elif now_month == 2:
                if (now_year % 4 == 0 and now_year % 100 != 0) or now_year % 400 == 0:
                    if now_day == 29:
                        now_day = 1
                        now_month += 1
                    else:
                        now_day += 1
                else:
                    if now_day == 28:
                        now_day = 1
                        now_month += 1
                    else:
                        now_day += 1
            dataQueue.put(goDate)
            print(goDate + "入队列")

#持续让日期出队列
class Store_data(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            if not dataQueue.empty():
                goDate = dataQueue.get()
                dataQueue.task_done()
                spider_job('青岛', '北京', goDate)
            else:
                break

def text(elements_list):
    elements_list = [i.text for i in elements_list]
    return elements_list


def spider_job(from_city, to_city, goDate):
    global content
    time.sleep(0.5)
    request_dic = {
        'depCity': from_city,
        'arrCity': to_city,
        'goDate': goDate
    }
    request_dic = parse.urlencode(request_dic)
    mobile_emulation = {"deviceName": "iPhone X"}
    options = Options()

    options.add_experimental_option("mobileEmulation", mobile_emulation)

    # 规避检测
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    driver = webdriver.Chrome(options=options)
    driver_url = 'https://m.flight.qunar.com/ncs/page/flightlist?%s&from=touch_index_' \
                 'search&child=0&baby=0&cabinType=0&_firstScreen=1&_gogokid=12' % request_dic
    driver.get(driver_url)
    print(driver_url)
    time.sleep(5)  #解决还未加载完网页就开始滑动，滑动失败的问题
    while True:
        try:
            # 屏幕向下滑动到最低端
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            more_list = driver.find_element_by_xpath(".//section[@class='list-getmore']")
            print(more_list.text)
            # 选择加载更多按钮并且点击
            driver.find_element_by_xpath(".//section[@class='list-getmore']").click()
            time.sleep(2.5)
        except:
            print('加载完毕')
            break

    from_time = text(driver.find_elements_by_xpath('//div[@class="from-info"]/p[1]'))
    from_airport = text(driver.find_elements_by_xpath('//div[@class="from-info"]/p[2]'))
    to_time = text(driver.find_elements_by_xpath('//div[@class="to-info"]/p[1]'))
    to_airport = text(driver.find_elements_by_xpath('//div[@class="to-info"]/p[2]'))
    company_info = text(driver.find_elements_by_xpath('//div[@class="company-info"]'))
    price = text(driver.find_elements_by_xpath('//p[@class="price-info"]'))

    for from_time, to_time, from_airport, to_airport, company ,price in zip(from_time, to_time, from_airport, to_airport, company_info, price):
        data = {
            '起飞时间': from_time,
            '抵达时间': to_time,
            '起飞机场': from_airport,
            '抵达机场': to_airport,
            '公司名称': company,
            '价格': price,
            '日期': goDate
        }
        content.append(data)
        print(data)
    driver.quit()

#计算时间
def gettimediff(start, end):
    seconds = (end - start).seconds
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    diff = ("%02d:%02d:%02d" % (h, m, s))
    return diff

if __name__ == '__main__':
    start = datetime.datetime.now()  # 开始时间
    find_data_thred = Find_date()  # 爬取的页数
    find_data_thred.start()
    t1 = []
    for i in range(3):  # 线程数
        store_data_thread = Store_data()
        store_data_thread.start()
        t1.append(store_data_thread)
    for t in t1:
        t.join()
        print("挂了")
    end = datetime.datetime.now()  # 结束时间
    diff = gettimediff(start, end)  # 计算耗时
    print('信息爬取完成共耗时: %s \n' % (diff))
    with open('青岛至北京航班信息.json', 'w') as fp:  # 将所得的数据存储为json文件
        fp.write(json.dumps(content, indent=2, ensure_ascii=False))