import json
import pygal
import re
filename = '青岛至北京航班信息.json'
with open(filename,encoding="utf-8") as f:
    datas = json.load(f)

list=[0]
list=list*120
a=b=c=d=e=f=0
day2=first_day=int(input('请输入数据开始的时间是几号：'))
month=int(datas[0]['日期'][5:7])
last_day=int(input('请输入'+str(month)+'月天数：'))
flag=0


for data in datas:
    day=data['日期']
    day1=day[8:10]
    time=data['起飞时间']
    time1=time[0:2]
    for x in range(0, 21):
        if (int(day1) == (x+int(first_day))):
            if (int(time1) >= 8 and int(time1) < 12):
                list[(x ) * 6 + 2] += 1
            elif (int(time1) >= 4 and int(time1) < 8):
                list[(x ) * 6 + 1] += 1
            elif (int(time1) >= 12 and int(time1) < 16):
                list[(x ) * 6 + 3] += 1
            elif (int(time1) >= 16 and int(time1) < 20):
                list[(x ) * 6 + 4] += 1
            elif (int(time1) >= 20 and int(time1) < 24):
                list[(x ) * 6 + 5] += 1
            elif (int(time1) >= 0 and int(time1) < 4):
                list[(x) * 6] += 1
            if(x+int(first_day)==last_day):
               flag+=1
               if(flag>30):
                    first_day=first_day-last_day

list1=[]
for x in range(0,120):
    d=day2
    if(x%6==0):
        d = str(month) + '-' + str(d) + '-' + '00-04'
        da = {d: list[x]}
        list1.append(da)
    elif(x%6==1):
        d = str(month) + '-' + str(d) + '-' + '04-08'
        da = {d: list[x]}
        list1.append(da)
    elif (x % 6 == 2):
        d = str(month) + '-' + str(d) + '-' + '08-12'
        da = {d: list[x]}
        list1.append(da)
    elif (x % 6 == 3):
        d = str(month) + '-' + str(d) + '-' + '12-16'
        da = {d: list[x]}
        list1.append(da)
    elif (x % 6 == 4):
        d = str(month) + '-' + str(d) + '-' + '16-20'
        da = {d: list[x]}
        list1.append(da)
    elif (x % 6 == 5):
        d = str(month) + '-' + str(d) + '-' + '20-24'
        da = {d: list[x]}
        list1.append(da)
        day2+=1
    if(day2==last_day+1):
        month+=1
        day2=1

with open('每四小时航班数.json', 'w',encoding="utf-8") as fp:  # 将所得的数据存储为json文件
    fp.write(json.dumps(list1, indent=2, ensure_ascii=False))
