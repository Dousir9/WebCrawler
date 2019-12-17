import json
import re

filename = "青岛至北京航班信息.json"

with open(filename) as f:
    datas = json.load(f)

shouhang = []
guohang = []
shanhang = []
xiahang = []
donghang = []
xinxilanhangkong = []
shenhang = []


for data in datas:
    name = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", data['公司名称'])
    name = name.split()[0]
    price = int(data['价格'])
    if name == "首航":
        info = {
            '航空公司': name,
            '日期': data['日期'],
            '起飞时间': data['起飞时间'],
            '价格': price
        }
        shouhang.append(info)
    elif name == '国航':
        info = {
            '航空公司': name,
            '日期': data['日期'],
            '起飞时间': data['起飞时间'],
            '价格': price
        }
        guohang.append(info)
    elif name == '山航':
        info = {
            '航空公司': name,
            '日期': data['日期'],
            '起飞时间': data['起飞时间'],
            '价格': price
        }
        shanhang.append(info)
    elif name == '厦航':
        info = {
            '航空公司': name,
            '日期': data['日期'],
            '起飞时间': data['起飞时间'],
            '价格': price
        }
        xiahang.append(info)
    elif name == '东航':
        info = {
            '航空公司': name,
            '日期': data['日期'],
            '起飞时间': data['起飞时间'],
            '价格': price
        }
        donghang.append(info)
    elif name == '新西兰航空':
        info = {
            '航空公司': name,
            '日期': data['日期'],
            '起飞时间': data['起飞时间'],
            '价格': price
        }
        xinxilanhangkong.append(info)
    elif name == '深航':
        info = {
            '航空公司': name,
            '日期': data['日期'],
            '起飞时间': data['起飞时间'],
            '价格': price
        }
        shenhang.append(info)

# 将所得的数据存储为json文件
with open('山航.json', 'w') as fp:
    fp.write(json.dumps(shanhang, indent=2, ensure_ascii=False))
with open('国航.json', 'w') as fp:
    fp.write(json.dumps(guohang, indent=2, ensure_ascii=False))
with open('厦航.json', 'w') as fp:
    fp.write(json.dumps(xiahang, indent=2, ensure_ascii=False))
with open('深航.json', 'w') as fp:
    fp.write(json.dumps(shenhang, indent=2, ensure_ascii=False))
with open('新西兰航空.json', 'w') as fp:
    fp.write(json.dumps(xinxilanhangkong, indent=2, ensure_ascii=False))
with open('东航.json', 'w') as fp:
    fp.write(json.dumps(donghang, indent=2, ensure_ascii=False))
with open('首航.json', 'w') as fp:
    fp.write(json.dumps(shouhang, indent=2, ensure_ascii=False))
