import json
import pygal

filename = '市北区清洗后.json'
with open(filename) as f:
    datas = json.load(f)

beiling = 0
beilingnum = 0
baolibaihe = 0
baolibaihenum = 0
beizhonglu = 0
beizhonglunum = 0
chongqingnanlu = 0
chongqingnanlunum = 0
changchunlu = 0
changchunlunum = 0
cuopuling = 0
cuopulingnum =0
dagang = 0
dagangnum = 0
dunhualu = 0
dunhualunum = 0
fushanhou = 0
fushanhounum = 0
fangzhongyuanshangyejie = 0
fangzhongyuanshangyejienum = 0
haiyunyan = 0
haiyunyannum = 0
hongshanbo = 0
hongshanbonum = 0
hangzhoulu = 0
hangzhoulunum = 0
haiboqiao = 0
haiboqiaonum = 0
hexi = 0
hexinum = 0
hudao = 0
hudaonum = 0
hefeilu = 0
hefeilunum = 0
jinhualu = 0
jinhualunum = 0
jiadingshan = 0
jiadingshannum = 0
jialinggou = 0
jialinggounum = 0
ligongdaxue = 0
ligongdaxuenum = 0
luoyanglu = 0
luoyanglunum = 0
renminlu = 0
renminlunum = 0
shandonglu = 0
shandonglunum = 0
shuiqinggou = 0
shuiqinggounum = 0
shiwuzhong = 0
shiwuzhongnum = 0
sifangliqun = 0
sifangliqunnum = 0
shibeizhoubian = 0
shibeizhoubiannum = 0
taidong = 0
taidongnum = 0
taiqinglu = 0
taiqinglunum = 0
taizhanlu = 0
taizhanlunum = 0
weihailu = 0
weihailunum = 0
xinxilu = 0
xinxilunum = 0
xinglonglu = 0
xinglonglunum = 0
xindouxin = 0
xindouxinnum = 0
yanjilu = 0
yanjilunum = 0
yanshanlijiaoqiao = 0
yanshanlijiaoqiaonum = 0
zhongyangshangwuqu = 0
zhongyangshangwuqunum = 0
zhenjianglu = 0
zhenjianglunum = 0

for data in datas:
    if data['地址'] == '北岭':
        beiling += data['平米单价']
        beilingnum += 1
    elif data['地址'] == '保利百合':
        baolibaihe += data['平米单价']
        baolibaihenum += 1
    elif data['地址'] == '北仲路':
        beizhonglu += data['平米单价']
        beizhonglunum += 1
    elif data['地址'] == '重庆南路':
        chongqingnanlu += data['平米单价']
        chongqingnanlunum += 1
    elif data['地址'] == '长春路':
        changchunlu += data['平米单价']
        changchunlunum += 1
    elif data['地址'] == '错埠岭':
        cuopuling += data['平米单价']
        cuopulingnum += 1
    elif data['地址'] == '大港':
        dagang += data['平米单价']
        dagangnum += 1
    elif data['地址'] == '敦化路':
        dunhualu += data['平米单价']
        dunhualunum += 1
    elif data['地址'] == '浮山后':
        fushanhou += data['平米单价']
        fushanhounum += 1
    elif data['地址'] == '方中圆商业街':
        fangzhongyuanshangyejie += data['平米单价']
        fangzhongyuanshangyejienum += 1
    elif data['地址'] == '海云庵':
        haiyunyan += data['平米单价']
        haiyunyannum += 1
    elif data['地址'] == '洪山坡':
        hongshanbo += data['平米单价']
        hongshanbonum += 1
    elif data['地址'] == '杭州路':
        hangzhoulu += data['平米单价']
        hangzhoulunum += 1
    elif data['地址'] == '海泊桥':
        haiboqiao += data['平米单价']
        haiboqiaonum += 1
    elif data['地址'] == '河西':
        hexi += data['平米单价']
        hexinum += 1
    elif data['地址'] == '湖岛':
        hudao += data['平米单价']
        hudaonum += 1
    elif data['地址'] == '合肥路':
        hefeilu += data['平米单价']
        hefeilunum += 1
    elif data['地址'] == '金华路':
        jinhualu += data['平米单价']
        jinhualunum += 1
    elif data['地址'] == '嘉定山':
        jiadingshan += data['平米单价']
        jiadingshannum += 1
    elif data['地址'] == '夹岭沟':
        jialinggou += data['平米单价']
        jialinggounum += 1
    elif data['地址'] == '理工大学':
        ligongdaxue += data['平米单价']
        ligongdaxuenum += 1
    elif data['地址'] == '洛阳路':
        luoyanglu += data['平米单价']
        luoyanglunum += 1
    elif data['地址'] == '人民路':
        renminlu += data['平米单价']
        renminlunum += 1
    elif data['地址'] == '水清沟':
        shuiqinggou += data['平米单价']
        shuiqinggounum += 1
    elif data['地址'] == '十五中':
        shiwuzhong += data['平米单价']
        shiwuzhongnum += 1
    elif data['地址'] == '四方利群':
        sifangliqun += data['平米单价']
        sifangliqunnum += 1
    elif data['地址'] == '市北周边':
        shibeizhoubian += data['平米单价']
        shibeizhoubiannum += 1
    elif data['地址'] == '台东':
        taidong += data['平米单价']
        taidongnum += 1
    elif data['地址'] == '太清路':
        taiqinglu += data['平米单价']
        taiqinglu += 1
    elif data['地址'] == '台湛路':
        taizhanlu += data['平米单价']
        taizhanlunum += 1
    elif data['地址'] == '威海路':
        weihailu += data['平米单价']
        weihailunum += 1
    elif data['地址'] == '信息城':
        xinxilu += data['平米单价']
        xinxilunum += 1
    elif data['地址'] == '兴隆路':
        xinglonglu += data['平米单价']
        xinglonglunum += 1
    elif data['地址'] == '新都心':
        xindouxin += data['平米单价']
        xindouxinnum += 1
    elif data['地址'] == '延吉路':
        yanjilu += data['平米单价']
        yanjilunum += 1
    elif data['地址'] == '燕山立交桥':
        yanshanlijiaoqiao += data['平米单价']
        yanshanlijiaoqiaonum += 1
    elif data['地址'] == '中央商务区':
        zhongyangshangwuqu += data['平米单价']
        zhongyangshangwuqunum += 1
    elif data['地址'] == '镇江路':
        zhenjianglu += data['平米单价']
        zhenjianglunum += 1

beiling = beiling / beilingnum
baolibaihe = baolibaihe / baolibaihenum
beizhonglu = beizhonglu / beizhonglunum
chongqingnanlu = chongqingnanlu / chongqingnanlunum
changchunlu = changchunlu / changchunlunum
cuopuling /= cuopulingnum
dagang /= dagangnum
dunhualu /= dunhualunum
fushanhou /= fushanhounum
fangzhongyuanshangyejie /= fangzhongyuanshangyejienum
haiyunyan /= haiyunyannum
hongshanbo /= hongshanbonum
hangzhoulu /= hangzhoulunum
haiboqiao /= haiboqiaonum
hexi /= hexinum
hudao /= hudaonum
hefeilu /= hefeilunum
jinhualu /= jinhualunum
jiadingshan /= jiadingshannum
jialinggou /= jialinggounum
ligongdaxue /= ligongdaxuenum
luoyanglu /= luoyanglunum
renminlu /= renminlunum
shuiqinggou /= shuiqinggounum
shiwuzhong /= shiwuzhongnum
sifangliqun /= sifangliqunnum

taidong /= taidongnum

taizhanlu /= taizhanlunum
weihailu /= weihailunum
xinxilu /= xinxilunum
xinglonglu /= xinglonglunum
xindouxin /= xindouxinnum
yanshanlijiaoqiao /= yanshanlijiaoqiaonum
zhongyangshangwuqu /= zhongyangshangwuqunum
zhenjianglu /= zhenjianglunum
average_price = []
average_price.append(beiling)
average_price.append(baolibaihe)
average_price.append(beizhonglu)
average_price.append(chongqingnanlu)
average_price.append(changchunlu)
average_price.append(cuopuling)
average_price.append(dagang)
average_price.append(dunhualu)
average_price.append(fushanhou)
average_price.append(fangzhongyuanshangyejie)
average_price.append(haiyunyan)
average_price.append(hongshanbo)
average_price.append(hangzhoulu)
average_price.append(haiboqiao)
average_price.append(hexi)
average_price.append(hudao)
average_price.append(hefeilu)
average_price.append(jinhualu)
average_price.append(jiadingshan)
average_price.append(jialinggou)
average_price.append(ligongdaxue)
average_price.append(luoyanglu)
average_price.append(renminlu)
average_price.append(shuiqinggou)
average_price.append(shiwuzhong)
average_price.append(sifangliqun)
average_price.append(taidong)
average_price.append(taizhanlu)
average_price.append(weihailu)
average_price.append(xinxilu)
average_price.append(xinglonglu)
average_price.append(xindouxin)
average_price.append(yanshanlijiaoqiao)
average_price.append(zhongyangshangwuqu)
average_price.append(zhenjianglu)

hist = pygal.Bar(x_label_rotation=50, style=pygal.style.DarkStyle)

hist.title = "市南区各个分区平均平米单价"
hist.x_labels = ['北岭', '保利百合', '北仲路', '重庆南路', '长春路', '错埠岭', '大港',
                 '敦化路', '浮山后', '方中圆商业街', '海云庵', '洪山坡', '杭州路', '海泊桥',
                 '河西', '湖岛', '合肥路', '金华路', '嘉定山', '夹岭沟', '理工大学', '洛阳路',
                 '人民路','水清沟', '十五中',
                 '四方利群', '台东', '台湛路', '威海路', '信息城', '兴隆路',
                 '新都心', '燕山立交桥', '中央商务区', '镇江路', ]
# hist.x_title = '分区'
hist.y_title = "平均平米单价"

hist.add("分区", average_price)
hist.render_to_file('市北区各个分区平均平米单价.svg')
