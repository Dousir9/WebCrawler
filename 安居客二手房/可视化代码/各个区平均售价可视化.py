import pygal
import json

filename1 = '市南区清洗后.json'
filename2 = '崂山区清洗后.json'
filename3 = "即墨市清洗后.json"
filename4 = "胶州市清洗后.json"
filename5 = "黄岛区清洗后.json"
filename6 = "城阳区清洗后.json"
filename7 = "市北区清洗后.json"
filename8 = "李沧区清洗后.json"
filename9 = "平度市清洗后.json"
filename10 = "莱西市清洗后.json"

with open(filename1) as f:
    shinanqu_data = json.load(f)
with open(filename2) as f:
    laoshanqu_data = json.load(f)
with open(filename3) as f:
    jimoshi_data = json.load(f)
with open(filename4) as f:
    jiaozhoushi_data = json.load(f)
with open(filename5) as f:
    huangdaoqu_data = json.load(f)
with open(filename6) as f:
    chengyangqu_data = json.load(f)
with open(filename7) as f:
    shibeiqu_data = json.load(f)
with open(filename8) as f:
    licangqu_data = json.load(f)
with open(filename9) as f:
    pingdushi_data = json.load(f)
with open(filename10) as f:
    laixishi_data = json.load(f)

sum = 0
for data in shinanqu_data:
    sum += data['平米单价']
average_price_1 = sum / len(shinanqu_data)

sum = 0
for data in laoshanqu_data:
    sum += data['平米单价']
average_price_2 = sum / len(laoshanqu_data)

sum = 0
for data in jimoshi_data:
    sum += data['平米单价']
average_price_3 = sum / len(jimoshi_data)

sum = 0
for data in jiaozhoushi_data:
    sum += data['平米单价']
average_price_4 = sum / len(jiaozhoushi_data)

sum = 0
for data in huangdaoqu_data:
    sum += data['平米单价']
average_price_5 = sum / len(huangdaoqu_data)

sum = 0
for data in chengyangqu_data:
    sum += data['平米单价']
average_price_6 = sum / len(chengyangqu_data)

sum = 0
for data in shibeiqu_data:
    sum += data['平米单价']
average_price_7 = sum / len(shibeiqu_data)

sum = 0
for data in licangqu_data:
    sum += data['平米单价']
average_price_8 = sum / len(licangqu_data)

sum = 0
for data in pingdushi_data:
    sum += data['平米单价']
average_price_9 = sum / len(pingdushi_data)

sum = 0
for data in laixishi_data:
    sum += data['平米单价']
average_price_10 = sum / len(laixishi_data)

average_price = []
average_price.append(average_price_1)
average_price.append(average_price_2)
average_price.append(average_price_3)
average_price.append(average_price_4)
average_price.append(average_price_5)
average_price.append(average_price_6)
average_price.append(average_price_7)
average_price.append(average_price_8)
average_price.append(average_price_9)
average_price.append(average_price_10)

hist = pygal.Bar(style=pygal.style.DarkStyle)

hist.title = "青岛市各区每平米平均售价"
hist.x_labels = ['市南区', '崂山区', '即墨市', '胶州市', '黄岛区', '城阳区', '市北区', '李沧区', '平度市', '莱西市']
hist.x_title = '区域'
hist.title = '各区每平米平均售价'
hist.y_title = "每平米平均售价"

hist.add('区域', average_price)
hist.render_to_file('青岛市各区每平米平均售价.svg')
