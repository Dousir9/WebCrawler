import pygal
import json

filename = "胶州市清洗后.json"
with open(filename) as f:
    datas = json.load(f)

beiguan = 0
beiguannum = 0
chanyexinqu = 0
chanyexinqunum = 0
fuan = 0
fuannum = 0
jiaozhouzhoubian = 0
jiaozhouzhoubiannum = 0
jiaodong = 0
jiaodongnum = 0
ligezhuang = 0
ligezhuangnum = 0
sanlihe = 0
sanlihenum = 0
xinchengqu = 0
xinchengqunum = 0
yunxi = 0
yunxinum = 0
zhongyun = 0
zhongyunnum = 0

for data in datas:
    if data['地址'] == '北关':
        beiguan += data['平米单价']
        beiguannum += 1
    elif data['地址'] == '产业新区':
        chanyexinqu += data['平米单价']
        chanyexinqunum += 1
    elif data['地址'] == '阜安':
        fuan += data['平米单价']
        fuannum += 1
    elif data['地址'] == '胶州周边':
        jiaozhouzhoubian += data['平米单价']
        jiaozhouzhoubiannum += 1
    elif data['地址'] == '胶东':
        jiaodong += data['平米单价']
        jiaodongnum += 1
    elif data['地址'] == '李哥庄':
        ligezhuang += data['平米单价']
        ligezhuangnum += 1
    elif data['地址'] == '三里河':
        sanlihe += data['平米单价']
        sanlihenum += 1
    elif data['地址'] == '新城区':
        xinchengqu += data['平米单价']
        xinchengqunum += 1
    elif data['地址'] == '云溪':
        yunxi += data['平米单价']
        yunxinum += 1
    elif data['地址'] == '中云':
        zhongyun += data['平米单价']
        zhongyunnum += 1

beiguan /= beiguannum
chanyexinqu /= chanyexinqunum
fuan /= fuannum
jiaozhouzhoubian /= jiaozhouzhoubiannum
jiaodong /= jiaodongnum
ligezhuang /= ligezhuangnum
sanlihe /= sanlihenum
xinchengqu /= xinchengqunum
yunxi /= yunxinum
zhongyun /= zhongyunnum

prices = []
prices.append(beiguan)
prices.append(chanyexinqu)
prices.append(fuan)
prices.append(jiaozhouzhoubian)
prices.append(jiaodong)
prices.append(ligezhuang)
prices.append(sanlihe)
prices.append(xinchengqu)
prices.append(yunxi)
prices.append(zhongyun)

hist = pygal.Bar(x_label_rotation=20, style=pygal.style.DarkStyle)

hist.title = "胶州市各分区平均平米单价"
hist.x_labels = ['北关', '产业新区', '阜安', '胶州周边', '胶东', '李哥庄', '三里河',
                 '新城区', '云溪', '中云', ]

hist.y_title = "平均平米单价"

hist.add('分区', prices)
hist.render_to_file('胶州市各个分区平均单价.svg')




























