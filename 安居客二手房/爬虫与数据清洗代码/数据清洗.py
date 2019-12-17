import json
import re

filename = '即墨市.json'
contents = []
with open(filename) as f:
    datas = json.load(f)
for data in datas:
    address = data['地址']
    averageprice = re.sub("\D", "", data['平米单价'])
    price = re.sub("\D", "", data['总价'])
    size = re.sub("\D+\D", "", data['大小'])
    data['总价'] = price
    averageprice = int(averageprice)
    price = int(price)
    size = float(size)
    print("{}".format(price))
    print("{}".format(averageprice))
    print("{}".format(size))
    content = {
        "地址": address,
        "总价": price,
        "平米单价": averageprice,
        "大小": size
    }
    contents.append(content)
with open('即墨市清洗后.json', 'w') as fp:  # 将所得的数据存储为json文件
    fp.write(json.dumps(contents, indent=2, ensure_ascii=False))
