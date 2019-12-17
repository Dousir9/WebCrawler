import json
import pygal

filename = '黄岛区清洗后.json'
with open(filename) as f:
    datas = json.load(f)

baoshuiqu = 0
baoshuiqunum = 0
changjianglu = 0
changjianglunum = 0
dongfangyingdu = 0
dongfangyingdunum = 0
hongshiya = 0
hongshiyanum = 0
huangdaozhoubian = 0
huangdaozhoubiannum = 0
jiaonanlaochengqu = 0
jiaonanlaochengqunum =0
lingshanwei = 0
lingshanweinum = 0
laohuangdao = 0
laohuangdaonum = 0
shiyoudaxue = 0
shiyoudaxuenum = 0
xinan = 0
xinannum = 0
xuejiadao = 0
xuejiadaonum = 0
xiangjianglu = 0
xiangjianglunum = 0
yinzhu = 0
yinzhunum = 0
zhushan = 0
zhushannum = 0

for data in datas:
    if data['地址'] == '保税区':
        baoshuiqu += data['平米单价']
        baoshuiqunum += 1
    elif data['地址'] == '长江路':
        changjianglu += data['平米单价']
        changjianglunum += 1
    elif data['地址'] == '东方影都':
        dongfangyingdu += data['平米单价']
        dongfangyingdunum += 1
    elif data['地址'] == '红石崖':
        hongshiya += data['平米单价']
        hongshiyanum += 1
    elif data['地址'] == '黄岛周边':
        huangdaozhoubian += data['平米单价']
        huangdaozhoubiannum += 1
    elif data['地址'] == '胶南老城区':
        jiaonanlaochengqu += data['平米单价']
        jiaonanlaochengqunum += 1
    elif data['地址'] == '灵山卫':
        lingshanwei += data['平米单价']
        lingshanweinum += 1
    elif data['地址'] == '老黄岛':
        laohuangdao += data['平米单价']
        laohuangdaonum += 1
    elif data['地址'] == '石油大学':
        shiyoudaxue += data['平米单价']
        shiyoudaxuenum += 1
    elif data['地址'] == '辛安':
        xinan += data['平米单价']
        xinannum += 1
    elif data['地址'] == '薛家岛':
        xuejiadao += data['平米单价']
        xuejiadaonum += 1
    elif data['地址'] == '香江路':
        xiangjianglu += data['平米单价']
        xiangjianglunum += 1
    elif data['地址'] == '隐珠':
        yinzhu += data['平米单价']
        yinzhunum += 1
    elif data['地址'] == '珠山':
        zhushan += data['平米单价']
        zhushannum += 1

baoshuiqu /= baoshuiqunum
changjianglu /= changjianglunum
dongfangyingdu /= dongfangyingdunum
hongshiya /= hongshiyanum
huangdaozhoubian /= huangdaozhoubiannum
jiaonanlaochengqu /= jiaonanlaochengqunum
lingshanwei /= lingshanweinum
laohuangdao /= laohuangdaonum
shiyoudaxue /= shiyoudaxuenum
xinan /= xinannum
xuejiadao /= xuejiadaonum
xiangjianglu /= xiangjianglunum
yinzhu /= yinzhunum
zhushan /= zhushannum

average_price = []
average_price.append(baoshuiqu)
average_price.append(changjianglu)
average_price.append(dongfangyingdu)
average_price.append(hongshiya)
average_price.append(huangdaozhoubian)
average_price.append(jiaonanlaochengqu)
average_price.append(lingshanwei)
average_price.append(laohuangdao)
average_price.append(shiyoudaxue)
average_price.append(xinan)
average_price.append(xuejiadao)
average_price.append(xiangjianglu)
average_price.append(yinzhu)
average_price.append(zhushan)

hist = pygal.Bar(x_label_rotation=40, style=pygal.style.DarkStyle)

hist.title = "黄岛区各个分区平均平米单价"
hist.x_labels = ['保税区', '长江路', '东方影都', '红石崖', '黄岛周边', '胶南老城区', '灵山卫',
                 '老黄岛', '石油大学', '辛安', '薛家岛', '香江路', '隐珠', '珠山']
# hist.x_title = '分区'
hist.y_title = "平均平米单价"

hist.add("分区", average_price)
hist.render_to_file('黄岛区各个分区平均平米单价.svg')
