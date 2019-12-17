import pygal
import json

filename = "崂山区清洗后.json"
with open(filename) as f:
    datas = json.load(f)

beicun = 0
beicunnum = 0
fushanqian = 0
fushanqiannum = 0
gaokeyuan = 0
gaokeyuannum = 0
laoshanquzhengfu = 0
laoshanquzhengfunum = 0
laoshanzhoubian = 0
laoshanzhoubiannum = 0
maidao = 0
maidaonum = 0
pijiucheng = 0
pijiuchengnum = 0
qichedongzhan = 0
qichedongzhannum = 0
qingdaoerzhong= 0
qingdaoerzhongnum = 0
shazikou = 0
shazikounum = 0
shilaoren = 0
shilaorennum = 0
yizhongtiyuchang = 0
yizhongtiyuchangnum = 0
zhonghan = 0
zhonghannum = 0

for data in datas:
    if data['地址'] == '北村':
        beicun += data['平米单价']
        beicunnum += 1
    elif data['地址'] == '浮山前':
        fushanqian += data['平米单价']
        fushanqiannum += 1
    elif data['地址'] == '高科园':
        gaokeyuan += data['平米单价']
        gaokeyuannum += 1
    elif data['地址'] == '崂山区政府':
        laoshanquzhengfu += data['平米单价']
        laoshanquzhengfunum += 1
    elif data['地址'] == '崂山周边':
        laoshanzhoubian += data['平米单价']
        laoshanzhoubiannum += 1
    elif data['地址'] == '麦岛':
        maidao += data['平米单价']
        maidaonum += 1
    elif data['地址'] == '啤酒城':
        pijiucheng += data['平米单价']
        pijiuchengnum += 1
    elif data['地址'] == '汽车东站':
        qichedongzhan += data['平米单价']
        qichedongzhannum += 1
    elif data['地址'] == '青岛二中':
        qingdaoerzhong += data['平米单价']
        qingdaoerzhongnum += 1
    elif data['地址'] == '沙子口':
        shazikou += data['平米单价']
        shazikounum += 1
    elif data['地址'] == '石老人':
        shilaoren += data['平米单价']
        shilaorennum += 1
    elif data['地址'] == '颐中体育场':
        yizhongtiyuchang += data['平米单价']
        yizhongtiyuchangnum += 1
    elif data['地址'] == '中韩':
        zhonghan += data['平米单价']
        zhonghannum += 1

beicun /= beicunnum
fushanqian /= fushanqiannum
gaokeyuan /= gaokeyuannum
laoshanquzhengfu /= laoshanquzhengfunum
laoshanzhoubian /= laoshanzhoubiannum
maidao /= maidaonum
pijiucheng /= pijiuchengnum
qichedongzhan /= qichedongzhannum
qingdaoerzhong /= qingdaoerzhongnum
shazikou /= shazikounum
shilaoren /= shilaorennum
yizhongtiyuchang /= yizhongtiyuchangnum
zhonghan /= zhonghannum

prices = []
prices.append(beicun)
prices.append(fushanqian)
prices.append(gaokeyuan)
prices.append(laoshanquzhengfu)
prices.append(laoshanzhoubian)
prices.append(maidao)
prices.append(pijiucheng)
prices.append(qichedongzhan)
prices.append(qingdaoerzhong)
prices.append(shazikou)
prices.append(shilaoren)
prices.append(yizhongtiyuchang)
prices.append(zhonghan)

hist = pygal.Bar(x_label_rotation=20, style=pygal.style.DarkStyle)

hist.title = "崂山区各分区平均平米单价"
hist.x_labels = ['北村', '浮山前', '高科园', '崂山区政府', '崂山周边', '麦岛',
                 '啤酒城', '汽车东站', '青岛二中', '沙子口', '石老人', '颐中体育场', '中韩']

hist.y_title = "平均平米单价"

hist.add('分区', prices)
hist.render_to_file('崂山区各个分区平均单价.svg')

