import json
import pygal

filename = "山航.json"

with open(filename) as f:
    datas = json.load(f)

start_date = '2019-11-11'
end_date = '2019-11-30'

now_year = int(start_date[0:4])
now_month = int(start_date[5:7])
now_day = int(start_date[8:10])

year = int(end_date[0:4])
month = int(end_date[5:7])
day = int(end_date[8:10])

date = []

while now_year < year or now_month < month or (now_month == month and now_day <= day):
    if now_month < 10:
        m = "0" + str(now_month)
    else:
        m = str(now_month)
    if now_day < 10:
        d = "0" + str(now_day)
    else:
        d = str(now_day)
    goDate = str(now_year) + "-" + m + "-" + d
    date.append(goDate)
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

price0 = 0
num0 = 0
price1 = 0
num1 = 0
price2 = 0
num2 = 0
price3 = 0
num3 = 0
price4 = 0
num4 = 0
price5 = 0
num5 = 0
price6 = 0
num6 = 0
price7 = 0
num7 = 0
price8 = 0
num8 = 0
price9 = 0
num9 = 0
price10 = 0
num10 = 0
price11 = 0
num11 = 0
price12 = 0
num12 = 0
price13 = 0
num13 = 0
price14 = 0
num14 = 0
price15 = 0
num15 = 0
price16 = 0
num16 = 0
price17 = 0
num17 = 0
price18 = 0
num18 = 0
price19 = 0
num19 = 0

for data in datas:
    if data['日期'] == date[0]:
        price0 += data['价格']
        num0 += 1
    elif data['日期'] == date[1]:
        price1 += data['价格']
        num1 += 1
    elif data['日期'] == date[2]:
        price2 += data['价格']
        num2 += 1
    elif data['日期'] == date[3]:
        price3 += data['价格']
        num3 += 1
    elif data['日期'] == date[4]:
        price4 += data['价格']
        num4 += 1
    elif data['日期'] == date[5]:
        price5 += data['价格']
        num5 += 1
    elif data['日期'] == date[6]:
        price6 += data['价格']
        num6 += 1
    elif data['日期'] == date[7]:
        price7 += data['价格']
        num7 += 1
    elif data['日期'] == date[8]:
        price8 += data['价格']
        num8 += 1
    elif data['日期'] == date[9]:
        price9 += data['价格']
        num9 += 1
    elif data['日期'] == date[10]:
        price10 += data['价格']
        num10 += 1
    elif data['日期'] == date[11]:
        price11 += data['价格']
        num11 += 1
    elif data['日期'] == date[12]:
        price12 += data['价格']
        num12 += 1
    elif data['日期'] == date[13]:
        price13 += data['价格']
        num13 += 1
    elif data['日期'] == date[14]:
        price14 += data['价格']
        num14 += 1
    elif data['日期'] == date[15]:
        price15 += data['价格']
        num15 += 1
    elif data['日期'] == date[16]:
        price16 += data['价格']
        num16 += 1
    elif data['日期'] == date[17]:
        price17 += data['价格']
        num17 += 1
    elif data['日期'] == date[18]:
        price18 += data['价格']
        num18 += 1
    elif data['日期'] == date[19]:
        price19 += data['价格']
        num19 += 1

price0 /= num0
price1 /= num1
price2 /= num2
price3 /= num3
price4 /= num4
price5 /= num5
price6 /= num6
price7 /= num7
price8 /= num8
price9 /= num9
price10 /= num10
price11 /= num11
price12 /= num12
price13 /= num13
price14 /= num14
price15 /= num15
price16 /= num16
price17 /= num17
price18 /= num18
price19 /= num19

average_price1 = []
average_price1.append(price1)
average_price1.append(price2)
average_price1.append(price3)
average_price1.append(price4)
average_price1.append(price5)
average_price1.append(price6)
average_price1.append(price7)
average_price1.append(price8)
average_price1.append(price9)
average_price1.append(price10)
average_price1.append(price11)
average_price1.append(price12)
average_price1.append(price13)
average_price1.append(price14)
average_price1.append(price15)
average_price1.append(price16)
average_price1.append(price17)
average_price1.append(price18)
average_price1.append(price19)

filename = "国航.json"

with open(filename) as f:
    datas = json.load(f)

price0 = 0
num0 = 0
price1 = 0
num1 = 0
price2 = 0
num2 = 0
price3 = 0
num3 = 0
price4 = 0
num4 = 0
price5 = 0
num5 = 0
price6 = 0
num6 = 0
price7 = 0
num7 = 0
price8 = 0
num8 = 0
price9 = 0
num9 = 0
price10 = 0
num10 = 0
price11 = 0
num11 = 0
price12 = 0
num12 = 0
price13 = 0
num13 = 0
price14 = 0
num14 = 0
price15 = 0
num15 = 0
price16 = 0
num16 = 0
price17 = 0
num17 = 0
price18 = 0
num18 = 0
price19 = 0
num19 = 0

for data in datas:
    if data['日期'] == date[0]:
        price0 += data['价格']
        num0 += 1
    elif data['日期'] == date[1]:
        price1 += data['价格']
        num1 += 1
    elif data['日期'] == date[2]:
        price2 += data['价格']
        num2 += 1
    elif data['日期'] == date[3]:
        price3 += data['价格']
        num3 += 1
    elif data['日期'] == date[4]:
        price4 += data['价格']
        num4 += 1
    elif data['日期'] == date[5]:
        price5 += data['价格']
        num5 += 1
    elif data['日期'] == date[6]:
        price6 += data['价格']
        num6 += 1
    elif data['日期'] == date[7]:
        price7 += data['价格']
        num7 += 1
    elif data['日期'] == date[8]:
        price8 += data['价格']
        num8 += 1
    elif data['日期'] == date[9]:
        price9 += data['价格']
        num9 += 1
    elif data['日期'] == date[10]:
        price10 += data['价格']
        num10 += 1
    elif data['日期'] == date[11]:
        price11 += data['价格']
        num11 += 1
    elif data['日期'] == date[12]:
        price12 += data['价格']
        num12 += 1
    elif data['日期'] == date[13]:
        price13 += data['价格']
        num13 += 1
    elif data['日期'] == date[14]:
        price14 += data['价格']
        num14 += 1
    elif data['日期'] == date[15]:
        price15 += data['价格']
        num15 += 1
    elif data['日期'] == date[16]:
        price16 += data['价格']
        num16 += 1
    elif data['日期'] == date[17]:
        price17 += data['价格']
        num17 += 1
    elif data['日期'] == date[18]:
        price18 += data['价格']
        num18 += 1
    elif data['日期'] == date[19]:
        price19 += data['价格']
        num19 += 1

price0 /= num0
price1 /= num1
price2 /= num2
price3 /= num3
price4 /= num4
price5 /= num5
price6 /= num6
price7 /= num7
price8 /= num8
price9 /= num9
price10 /= num10
price11 /= num11
price12 /= num12
price13 /= num13
price14 /= num14
price15 /= num15
price16 /= num16
price17 /= num17
price18 /= num18
price19 /= num19

average_price2 = []
average_price2.append(price1)
average_price2.append(price2)
average_price2.append(price3)
average_price2.append(price4)
average_price2.append(price5)
average_price2.append(price6)
average_price2.append(price7)
average_price2.append(price8)
average_price2.append(price9)
average_price2.append(price10)
average_price2.append(price11)
average_price2.append(price12)
average_price2.append(price13)
average_price2.append(price14)
average_price2.append(price15)
average_price2.append(price16)
average_price2.append(price17)
average_price2.append(price18)
average_price2.append(price19)


filename = "深航.json"

with open(filename) as f:
    datas = json.load(f)

price0 = 0
num0 = 0
price1 = 0
num1 = 0
price2 = 0
num2 = 0
price3 = 0
num3 = 0
price4 = 0
num4 = 0
price5 = 0
num5 = 0
price6 = 0
num6 = 0
price7 = 0
num7 = 0
price8 = 0
num8 = 0
price9 = 0
num9 = 0
price10 = 0
num10 = 0
price11 = 0
num11 = 0
price12 = 0
num12 = 0
price13 = 0
num13 = 0
price14 = 0
num14 = 0
price15 = 0
num15 = 0
price16 = 0
num16 = 0
price17 = 0
num17 = 0
price18 = 0
num18 = 0
price19 = 0
num19 = 0

for data in datas:
    if data['日期'] == date[0]:
        price0 += data['价格']
        num0 += 1
    elif data['日期'] == date[1]:
        price1 += data['价格']
        num1 += 1
    elif data['日期'] == date[2]:
        price2 += data['价格']
        num2 += 1
    elif data['日期'] == date[3]:
        price3 += data['价格']
        num3 += 1
    elif data['日期'] == date[4]:
        price4 += data['价格']
        num4 += 1
    elif data['日期'] == date[5]:
        price5 += data['价格']
        num5 += 1
    elif data['日期'] == date[6]:
        price6 += data['价格']
        num6 += 1
    elif data['日期'] == date[7]:
        price7 += data['价格']
        num7 += 1
    elif data['日期'] == date[8]:
        price8 += data['价格']
        num8 += 1
    elif data['日期'] == date[9]:
        price9 += data['价格']
        num9 += 1
    elif data['日期'] == date[10]:
        price10 += data['价格']
        num10 += 1
    elif data['日期'] == date[11]:
        price11 += data['价格']
        num11 += 1
    elif data['日期'] == date[12]:
        price12 += data['价格']
        num12 += 1
    elif data['日期'] == date[13]:
        price13 += data['价格']
        num13 += 1
    elif data['日期'] == date[14]:
        price14 += data['价格']
        num14 += 1
    elif data['日期'] == date[15]:
        price15 += data['价格']
        num15 += 1
    elif data['日期'] == date[16]:
        price16 += data['价格']
        num16 += 1
    elif data['日期'] == date[17]:
        price17 += data['价格']
        num17 += 1
    elif data['日期'] == date[18]:
        price18 += data['价格']
        num18 += 1
    elif data['日期'] == date[19]:
        price19 += data['价格']
        num19 += 1

price0 /= num0
price1 /= num1
price2 /= num2
price3 /= num3
price4 /= num4
price5 /= num5
price6 /= num6
price7 /= num7
price8 /= num8
price9 /= num9
price10 /= num10
price11 /= num11
price12 /= num12
price13 /= num13
price14 /= num14
price15 /= num15
price16 /= num16
price17 /= num17
price18 /= num18
price19 /= num19

average_price3 = []
average_price3.append(price1)
average_price3.append(price2)
average_price3.append(price3)
average_price3.append(price4)
average_price3.append(price5)
average_price3.append(price6)
average_price3.append(price7)
average_price3.append(price8)
average_price3.append(price9)
average_price3.append(price10)
average_price3.append(price11)
average_price3.append(price12)
average_price3.append(price13)
average_price3.append(price14)
average_price3.append(price15)
average_price3.append(price16)
average_price3.append(price17)
average_price3.append(price18)
average_price3.append(price19)


filename = "东航.json"

with open(filename) as f:
    datas = json.load(f)

price0 = 0
num0 = 0
price1 = 0
num1 = 0
price2 = 0
num2 = 0
price3 = 0
num3 = 0
price4 = 0
num4 = 0
price5 = 0
num5 = 0
price6 = 0
num6 = 0
price7 = 0
num7 = 0
price8 = 0
num8 = 0
price9 = 0
num9 = 0
price10 = 0
num10 = 0
price11 = 0
num11 = 0
price12 = 0
num12 = 0
price13 = 0
num13 = 0
price14 = 0
num14 = 0
price15 = 0
num15 = 0
price16 = 0
num16 = 0
price17 = 0
num17 = 0
price18 = 0
num18 = 0
price19 = 0
num19 = 0

for data in datas:
    if data['日期'] == date[0]:
        price0 += data['价格']
        num0 += 1
    elif data['日期'] == date[1]:
        price1 += data['价格']
        num1 += 1
    elif data['日期'] == date[2]:
        price2 += data['价格']
        num2 += 1
    elif data['日期'] == date[3]:
        price3 += data['价格']
        num3 += 1
    elif data['日期'] == date[4]:
        price4 += data['价格']
        num4 += 1
    elif data['日期'] == date[5]:
        price5 += data['价格']
        num5 += 1
    elif data['日期'] == date[6]:
        price6 += data['价格']
        num6 += 1
    elif data['日期'] == date[7]:
        price7 += data['价格']
        num7 += 1
    elif data['日期'] == date[8]:
        price8 += data['价格']
        num8 += 1
    elif data['日期'] == date[9]:
        price9 += data['价格']
        num9 += 1
    elif data['日期'] == date[10]:
        price10 += data['价格']
        num10 += 1
    elif data['日期'] == date[11]:
        price11 += data['价格']
        num11 += 1
    elif data['日期'] == date[12]:
        price12 += data['价格']
        num12 += 1
    elif data['日期'] == date[13]:
        price13 += data['价格']
        num13 += 1
    elif data['日期'] == date[14]:
        price14 += data['价格']
        num14 += 1
    elif data['日期'] == date[15]:
        price15 += data['价格']
        num15 += 1
    elif data['日期'] == date[16]:
        price16 += data['价格']
        num16 += 1
    elif data['日期'] == date[17]:
        price17 += data['价格']
        num17 += 1
    elif data['日期'] == date[18]:
        price18 += data['价格']
        num18 += 1
    elif data['日期'] == date[19]:
        price19 += data['价格']
        num19 += 1

price0 /= num0
price1 /= num1
price2 /= num2
price3 /= num3
price4 /= num4
price5 /= num5
price6 /= num6
price7 /= num7
price8 /= num8
price9 /= num9
price10 /= num10
price11 /= num11
price12 /= num12
price13 /= num13
price14 /= num14
price15 /= num15
price16 /= num16
price17 /= num17
price18 /= num18
price19 /= num19

average_price4 = []
average_price4.append(price1)
average_price4.append(price2)
average_price4.append(price3)
average_price4.append(price4)
average_price4.append(price5)
average_price4.append(price6)
average_price4.append(price7)
average_price4.append(price8)
average_price4.append(price9)
average_price4.append(price10)
average_price4.append(price11)
average_price4.append(price12)
average_price4.append(price13)
average_price4.append(price14)
average_price4.append(price15)
average_price4.append(price16)
average_price4.append(price17)
average_price4.append(price18)
average_price4.append(price19)

filename = "首航.json"

with open(filename) as f:
    datas = json.load(f)

price0 = 0
num0 = 0
price1 = 0
num1 = 0
price2 = 0
num2 = 0
price3 = 0
num3 = 0
price4 = 0
num4 = 0
price5 = 0
num5 = 0
price6 = 0
num6 = 0
price7 = 0
num7 = 0
price8 = 0
num8 = 0
price9 = 0
num9 = 0
price10 = 0
num10 = 0
price11 = 0
num11 = 0
price12 = 0
num12 = 0
price13 = 0
num13 = 0
price14 = 0
num14 = 0
price15 = 0
num15 = 0
price16 = 0
num16 = 0
price17 = 0
num17 = 0
price18 = 0
num18 = 0
price19 = 0
num19 = 0

for data in datas:
    if data['日期'] == date[0]:
        price0 += data['价格']
        num0 += 1
    elif data['日期'] == date[1]:
        price1 += data['价格']
        num1 += 1
    elif data['日期'] == date[2]:
        price2 += data['价格']
        num2 += 1
    elif data['日期'] == date[3]:
        price3 += data['价格']
        num3 += 1
    elif data['日期'] == date[4]:
        price4 += data['价格']
        num4 += 1
    elif data['日期'] == date[5]:
        price5 += data['价格']
        num5 += 1
    elif data['日期'] == date[6]:
        price6 += data['价格']
        num6 += 1
    elif data['日期'] == date[7]:
        price7 += data['价格']
        num7 += 1
    elif data['日期'] == date[8]:
        price8 += data['价格']
        num8 += 1
    elif data['日期'] == date[9]:
        price9 += data['价格']
        num9 += 1
    elif data['日期'] == date[10]:
        price10 += data['价格']
        num10 += 1
    elif data['日期'] == date[11]:
        price11 += data['价格']
        num11 += 1
    elif data['日期'] == date[12]:
        price12 += data['价格']
        num12 += 1
    elif data['日期'] == date[13]:
        price13 += data['价格']
        num13 += 1
    elif data['日期'] == date[14]:
        price14 += data['价格']
        num14 += 1
    elif data['日期'] == date[15]:
        price15 += data['价格']
        num15 += 1
    elif data['日期'] == date[16]:
        price16 += data['价格']
        num16 += 1
    elif data['日期'] == date[17]:
        price17 += data['价格']
        num17 += 1
    elif data['日期'] == date[18]:
        price18 += data['价格']
        num18 += 1
    elif data['日期'] == date[19]:
        price19 += data['价格']
        num19 += 1

price0 /= num0
price1 /= num1
price2 /= num2
price3 /= num3
price4 /= num4
price5 /= num5
price6 /= num6
price7 /= num7
price8 /= num8
price9 /= num9
price10 /= num10
price11 /= num11
price12 /= num12
price13 /= num13
price14 /= num14
price15 /= num15
price16 /= num16
price17 /= num17
price18 /= num18
price19 /= num19

average_price5 = []
average_price5.append(price1)
average_price5.append(price2)
average_price5.append(price3)
average_price5.append(price4)
average_price5.append(price5)
average_price5.append(price6)
average_price5.append(price7)
average_price5.append(price8)
average_price5.append(price9)
average_price5.append(price10)
average_price5.append(price11)
average_price5.append(price12)
average_price5.append(price13)
average_price5.append(price14)
average_price5.append(price15)
average_price5.append(price16)
average_price5.append(price17)
average_price5.append(price18)
average_price5.append(price19)


filename = "厦航.json"

with open(filename) as f:
    datas = json.load(f)

price0 = 0
num0 = 0
price1 = 0
num1 = 0
price2 = 0
num2 = 0
price3 = 0
num3 = 0
price4 = 0
num4 = 0
price5 = 0
num5 = 0
price6 = 0
num6 = 0
price7 = 0
num7 = 0
price8 = 0
num8 = 0
price9 = 0
num9 = 0
price10 = 0
num10 = 0
price11 = 0
num11 = 0
price12 = 0
num12 = 0
price13 = 0
num13 = 0
price14 = 0
num14 = 0
price15 = 0
num15 = 0
price16 = 0
num16 = 0
price17 = 0
num17 = 0
price18 = 0
num18 = 0
price19 = 0
num19 = 0

for data in datas:
    if data['日期'] == date[0]:
        price0 += data['价格']
        num0 += 1
    elif data['日期'] == date[1]:
        price1 += data['价格']
        num1 += 1
    elif data['日期'] == date[2]:
        price2 += data['价格']
        num2 += 1
    elif data['日期'] == date[3]:
        price3 += data['价格']
        num3 += 1
    elif data['日期'] == date[4]:
        price4 += data['价格']
        num4 += 1
    elif data['日期'] == date[5]:
        price5 += data['价格']
        num5 += 1
    elif data['日期'] == date[6]:
        price6 += data['价格']
        num6 += 1
    elif data['日期'] == date[7]:
        price7 += data['价格']
        num7 += 1
    elif data['日期'] == date[8]:
        price8 += data['价格']
        num8 += 1
    elif data['日期'] == date[9]:
        price9 += data['价格']
        num9 += 1
    elif data['日期'] == date[10]:
        price10 += data['价格']
        num10 += 1
    elif data['日期'] == date[11]:
        price11 += data['价格']
        num11 += 1
    elif data['日期'] == date[12]:
        price12 += data['价格']
        num12 += 1
    elif data['日期'] == date[13]:
        price13 += data['价格']
        num13 += 1
    elif data['日期'] == date[14]:
        price14 += data['价格']
        num14 += 1
    elif data['日期'] == date[15]:
        price15 += data['价格']
        num15 += 1
    elif data['日期'] == date[16]:
        price16 += data['价格']
        num16 += 1
    elif data['日期'] == date[17]:
        price17 += data['价格']
        num17 += 1
    elif data['日期'] == date[18]:
        price18 += data['价格']
        num18 += 1
    elif data['日期'] == date[19]:
        price19 += data['价格']
        num19 += 1

price0 /= num0
price1 /= num1
price2 /= num2
price3 /= num3
price4 /= num4
price5 /= num5
price6 /= num6
price7 /= num7
price8 /= num8
price9 /= num9
price10 /= num10
price11 /= num11
price12 /= num12
price13 /= num13
price14 /= num14
price15 /= num15
price16 /= num16
price17 /= num17
price18 /= num18
price19 /= num19

average_price6 = []
average_price6.append(price1)
average_price6.append(price2)
average_price6.append(price3)
average_price6.append(price4)
average_price6.append(price5)
average_price6.append(price6)
average_price6.append(price7)
average_price6.append(price8)
average_price6.append(price9)
average_price6.append(price10)
average_price6.append(price11)
average_price6.append(price12)
average_price6.append(price13)
average_price6.append(price14)
average_price6.append(price15)
average_price6.append(price16)
average_price6.append(price17)
average_price6.append(price18)
average_price6.append(price19)

filename = "新西兰航空.json"

with open(filename) as f:
    datas = json.load(f)

price0 = 0
num0 = 0
price1 = 0
num1 = 0
price2 = 0
num2 = 0
price3 = 0
num3 = 0
price4 = 0
num4 = 0
price5 = 0
num5 = 0
price6 = 0
num6 = 0
price7 = 0
num7 = 0
price8 = 0
num8 = 0
price9 = 0
num9 = 0
price10 = 0
num10 = 0
price11 = 0
num11 = 0
price12 = 0
num12 = 0
price13 = 0
num13 = 0
price14 = 0
num14 = 0
price15 = 0
num15 = 0
price16 = 0
num16 = 0
price17 = 0
num17 = 0
price18 = 0
num18 = 0
price19 = 0
num19 = 0

for data in datas:
    if data['日期'] == date[0]:
        price0 += data['价格']
        num0 += 1
    elif data['日期'] == date[1]:
        price1 += data['价格']
        num1 += 1
    elif data['日期'] == date[2]:
        price2 += data['价格']
        num2 += 1
    elif data['日期'] == date[3]:
        price3 += data['价格']
        num3 += 1
    elif data['日期'] == date[4]:
        price4 += data['价格']
        num4 += 1
    elif data['日期'] == date[5]:
        price5 += data['价格']
        num5 += 1
    elif data['日期'] == date[6]:
        price6 += data['价格']
        num6 += 1
    elif data['日期'] == date[7]:
        price7 += data['价格']
        num7 += 1
    elif data['日期'] == date[8]:
        price8 += data['价格']
        num8 += 1
    elif data['日期'] == date[9]:
        price9 += data['价格']
        num9 += 1
    elif data['日期'] == date[10]:
        price10 += data['价格']
        num10 += 1
    elif data['日期'] == date[11]:
        price11 += data['价格']
        num11 += 1
    elif data['日期'] == date[12]:
        price12 += data['价格']
        num12 += 1
    elif data['日期'] == date[13]:
        price13 += data['价格']
        num13 += 1
    elif data['日期'] == date[14]:
        price14 += data['价格']
        num14 += 1
    elif data['日期'] == date[15]:
        price15 += data['价格']
        num15 += 1
    elif data['日期'] == date[16]:
        price16 += data['价格']
        num16 += 1
    elif data['日期'] == date[17]:
        price17 += data['价格']
        num17 += 1
    elif data['日期'] == date[18]:
        price18 += data['价格']
        num18 += 1
    elif data['日期'] == date[19]:
        price19 += data['价格']
        num19 += 1

price0 /= num0
price1 /= num1
price2 /= num2
price3 /= num3
price4 /= num4
price5 /= num5
price6 /= num6
price7 /= num7
price8 /= num8
price9 /= num9
price10 /= num10
price11 /= num11
price12 /= num12
price13 /= num13
price14 /= num14
price15 /= num15
price16 /= num16
price17 /= num17
price18 /= num18
price19 /= num19

average_price7 = []
average_price7.append(price1)
average_price7.append(price2)
average_price7.append(price3)
average_price7.append(price4)
average_price7.append(price5)
average_price7.append(price6)
average_price7.append(price7)
average_price7.append(price8)
average_price7.append(price9)
average_price7.append(price10)
average_price7.append(price11)
average_price7.append(price12)
average_price7.append(price13)
average_price7.append(price14)
average_price7.append(price15)
average_price7.append(price16)
average_price7.append(price17)
average_price7.append(price18)
average_price7.append(price19)


line_chart = pygal.Line(x_label_rotation = 30)
# style=pygal.style.DarkStyle
line_chart.title = "青岛至北京20天机票价格走势图11.11"
line_chart.x_labels = date

line_chart.add('山航', average_price1)
line_chart.add('国航', average_price2)
line_chart.add('深航', average_price3)
line_chart.add('东航', average_price4)
line_chart.add('首航', average_price5)
line_chart.add('厦航', average_price6)
line_chart.add('新西兰航空', average_price7)


line_chart.render_to_file("青岛至北京20天机票价格走势图11.11.svg")







