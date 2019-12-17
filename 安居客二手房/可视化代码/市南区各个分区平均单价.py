import json
import pygal

filename = '市南区清洗后.json'
with open(filename) as f:
    datas = json.load(f)

aofanzhongxin = 0
aofanzhongxinnum = 0
badaguan = 0
badaguannum = 0
badahu = 0
badahunum = 0
badaxia = 0
badaxianum = 0
daxuelu = 0
daxuelunum = 0
donghaixilu = 0
donghaixilunum = 0
dayao = 0
dayaonum = 0
fushansuo = 0
fushansuonum = 0
fuzhounanlu = 0
fuzhounanlunum = 0
guangdiandasha = 0
guangdiandashanum = 0
huochezhan = 0
huochezhannum = 0
jiangxilu = 0
jiangxilunum = 0
minjianglu = 0
minjianglunum = 0
ningxialu = 0
ningxialunum = 0
qingdaodaxue = 0
qingdaodaxuenum = 0
shaoxinglu = 0
shaoxinglunum = 0
shinanzhoubian = 0
shinanzhoubiannum = 0
tianshan = 0
tianshannum = 0
tuandao = 0
tuandaonum = 0
wusiguangchang = 0
wusiguangchangnum = 0
xuzhoulu = 0
xuzhoulunum = 0
xianggangzhonglu = 0
xianggangzhonglunum = 0
xizhen = 0
xizhennum = 0
xinjiazhuang = 0
xinjiazhuangnum = 0
yanansanlu = 0
yanansanlunum = 0
yanerdaolu = 0
yanerdaolunum = 0
zhanshan = 0
zhanshannum = 0
zhongshanlu = 0
zhongshanlunum = 0
zhiquanlu = 0
zhiquanlunum = 0

for data in datas:
    if data['地址'] == '奥帆中心':
        aofanzhongxin += data['平米单价']
        aofanzhongxinnum += 1
    elif data['地址'] == '八大关':
        badaguan += data['平米单价']
        badaguannum += 1
    elif data['地址'] == '八大湖':
        badahu += data['平米单价']
        badahunum += 1
    elif data['地址'] == '八大峡':
        badaxia += data['平米单价']
        badaxianum += 1
    elif data['地址'] == '大学路':
        daxuelu += data['平米单价']
        daxuelunum += 1
    elif data['地址'] == '东海西路':
        donghaixilu += data['平米单价']
        donghaixilunum += 1
    elif data['地址'] == '大尧':
        dayao += data['平米单价']
        dayaonum += 1
    elif data['地址'] == '浮山所':
        fushansuo += data['平米单价']
        fushansuonum += 1
    elif data['地址'] == '福州南路':
        fuzhounanlu += data['平米单价']
        fuzhounanlunum += 1
    elif data['地址'] == '广电大厦':
        guangdiandasha += data['平米单价']
        guangdiandashanum += 1
    elif data['地址'] == '火车站':
        huochezhan += data['平米单价']
        huochezhannum += 1
    elif data['地址'] == '江西路':
        jiangxilu += data['平米单价']
        jiangxilunum += 1
    elif data['地址'] == '闽江路':
        minjianglu += data['平米单价']
        minjianglunum += 1
    elif data['地址'] == '宁夏路':
        ningxialu += data['平米单价']
        ningxialunum += 1
    elif data['地址'] == '青岛大学':
        qingdaodaxue += data['平米单价']
        qingdaodaxuenum += 1
    elif data['地址'] == '绍兴路':
        shaoxinglu += data['平米单价']
        shaoxinglunum += 1
    elif data['地址'] == '市南周边':
        shinanzhoubian += data['平米单价']
        shinanzhoubiannum += 1
    elif data['地址'] == '天山':
        tianshan += data['平米单价']
        tianshannum += 1
    elif data['地址'] == '团岛':
        tuandao += data['平米单价']
        tuandaonum += 1
    elif data['地址'] == '五四广场':
        wusiguangchang += data['平米单价']
        wusiguangchangnum += 1
    elif data['地址'] == '徐州路':
        xuzhoulu += data['平米单价']
        xuzhoulunum += 1
    elif data['地址'] == '香港中路':
        xianggangzhonglu += data['平米单价']
        xianggangzhonglunum += 1
    elif data['地址'] == '西镇':
        xizhen += data['平米单价']
        xizhennum += 1
    elif data['地址'] == '辛家庄':
        xinjiazhuang += data['平米单价']
        xinjiazhuangnum += 1
    elif data['地址'] == '延安三路':
        yanansanlu += data['平米单价']
        yanansanlunum += 1
    elif data['地址'] == '燕儿岛路':
        yanerdaolu += data['平米单价']
        yanerdaolunum += 1
    elif data['地址'] == '湛山':
        zhanshan += data['平米单价']
        zhanshannum += 1
    elif data['地址'] == '中山路':
        zhongshanlu += data['平米单价']
        zhongshanlunum += 1
    elif data['地址'] == '芝泉路':
        zhiquanlu += data['平米单价']
        zhiquanlunum += 1

aofanzhongxin = aofanzhongxin / aofanzhongxinnum
badaguan = badaguan / badaxianum
badahu = badahu / badaxianum
badaxia = badaxia / badaxianum
daxuelu = daxuelu / daxuelunum
donghaixilu /= donghaixilunum
dayao /= dayaonum
fushansuo /= fushansuonum
fuzhounanlu /= fuzhounanlunum
guangdiandasha /= guangdiandashanum
huochezhan /= huochezhannum
jiangxilu /= jiangxilunum
minjianglu /= minjianglunum
ningxialu /= ningxialunum
qingdaodaxue /= qingdaodaxuenum
shaoxinglu /= shaoxinglunum
shinanzhoubian /= shinanzhoubiannum
tianshan /= tianshannum
tuandao /= tuandaonum
wusiguangchang /= wusiguangchangnum
xuzhoulu /= xuzhoulunum
xianggangzhonglu /= xianggangzhonglunum
xizhen /= xizhennum
xinjiazhuang /= xinjiazhuangnum
yanansanlu /= yanansanlunum
yanerdaolu /= yanerdaolunum
zhanshan /= zhanshannum
zhongshanlu /= zhongshanlunum
zhiquanlu /= zhiquanlunum
average_price = []
average_price.append(aofanzhongxin)
average_price.append(badaguan)
average_price.append(badahu)
average_price.append(badaxia)
average_price.append(daxuelu)
average_price.append(donghaixilu)
average_price.append(dayao)
average_price.append(fushansuo)
average_price.append(fuzhounanlu)
average_price.append(guangdiandasha)
average_price.append(huochezhan)
average_price.append(jiangxilu)
average_price.append(minjianglu)
average_price.append(ningxialu)
average_price.append(qingdaodaxue)
average_price.append(shaoxinglu)
average_price.append(shinanzhoubian)
average_price.append(tianshan)
average_price.append(tuandao)
average_price.append(wusiguangchang)
average_price.append(xuzhoulu)
average_price.append(xianggangzhonglu)
average_price.append(xizhen)
average_price.append(xinjiazhuang)
average_price.append(yanansanlu)
average_price.append(yanerdaolu)
average_price.append(zhanshan)
average_price.append(zhongshanlu)
average_price.append(zhiquanlu)

hist = pygal.Bar(x_label_rotation=40,  style=pygal.style.DarkStyle)

hist.title = "市南区各个分区平均平米单价"
hist.x_labels = ['奥帆中心', '八大关', '八大湖', '八大峡', '大学路', '东海西路', '大尧',
                 '浮山所', '福州南路', '广电大厦', '火车站', '江西路', '闽江路', '宁夏路', '青岛大学',
                 '绍兴路', '市南周边', '天山', '团岛', '五四广场', '徐州路', '香港中路', '西镇', '辛家庄',
                 '延安三路', '燕儿岛路', '湛山', '中山路', '芝泉路']
# hist.x_title = '分区'
hist.y_title = "平均平米单价"

hist.add("分区", average_price)
hist.render_to_file('市南区各个分区平均平米单价.svg')