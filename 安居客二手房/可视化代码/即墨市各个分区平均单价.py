import pygal
import json

filename = "即墨市清洗后.json"
with open(filename) as f:
    datas = json.load(f)

aoshanweizhen = 0
aoshanweizhennum = 0
chaohai = 0
chaohainum = 0
chuangzhixinqu = 0
chuangzhixinqunum = 0
darunfa = 0
darunfanum = 0
ershibazhong = 0
ershibazhongnum = 0
huanxiu = 0
huanxiunum = 0
hepingqu = 0
hepingqunum = 0
jimozhoubian = 0
jimozhoubiannum = 0
jimobaolongchengshiguangchang = 0
jimobaolongchengshiguangchangnum = 0
kaifaqu = 0
kaifaqunum = 0
lanseguigu = 0
lanseguigunum = 0
liantongdasha = 0
liantongdashanum = 0
mingduyuan = 0
mingduyuannum = 0
tongji = 0
tongjinum = 0
xinqichezhan = 0
xinqichezhannum = 0
xiyuanzhuang = 0
xiyuanzhuangnum = 0

for data in datas:
    if data['地址'] == '鳌山卫镇':
        aoshanweizhen += data['平米单价']
        aoshanweizhennum += 1
    elif data['地址'] == '潮海':
        chaohai += data['平米单价']
        chaohainum += 1
    elif data['地址'] == '创智新区':
        chuangzhixinqu += data['平米单价']
        chuangzhixinqunum += 1
    elif data['地址'] == '大润发':
        darunfa += data['平米单价']
        darunfanum += 1
    elif data['地址'] == '二十八中':
        ershibazhong += data['平米单价']
        ershibazhongnum += 1
    elif data['地址'] == '环秀':
        huanxiu += data['平米单价']
        huanxiunum += 1
    elif data['地址'] == '和平区':
        hepingqu += data['平米单价']
        hepingqunum += 1
    elif data['地址'] == '即墨周边':
        jimozhoubian += data['平米单价']
        jimozhoubiannum += 1
    elif data['地址'] == '即墨宝龙城市广场':
        jimobaolongchengshiguangchang += data['平米单价']
        jimobaolongchengshiguangchangnum += 1
    elif data['地址'] == '开发区':
        kaifaqu += data['平米单价']
        kaifaqunum += 1
    elif data['地址'] == '蓝色硅谷':
        lanseguigu += data['平米单价']
        lanseguigunum += 1
    elif data['地址'] == '联通大厦':
        liantongdasha += data['平米单价']
        liantongdashanum += 1
    elif data['地址'] == '名都苑':
        mingduyuan += data['平米单价']
        mingduyuannum += 1
    elif data['地址'] == '通济':
        tongji += data['平米单价']
        tongjinum += 1
    elif data['地址'] == '新汽车站':
        xinqichezhan += data['平米单价']
        xinqichezhannum += 1
    elif data['地址'] == '西元庄':
        xiyuanzhuang += data['平米单价']
        xiyuanzhuangnum += 1

aoshanweizhen /= aoshanweizhennum
chaohai /= chaohainum
chuangzhixinqu /= chuangzhixinqunum
darunfa /= darunfanum
ershibazhong /= ershibazhongnum
huanxiu /= huanxiunum
hepingqu /= hepingqunum
jimozhoubian /= jimozhoubiannum
jimobaolongchengshiguangchang /= jimobaolongchengshiguangchangnum
kaifaqu /= kaifaqunum
lanseguigu /= lanseguigunum
liantongdasha /= liantongdashanum
mingduyuan /= mingduyuannum
tongji /= tongjinum
xinqichezhan /= xinqichezhannum
xiyuanzhuang /= xiyuanzhuangnum

prices = []
prices.append(aoshanweizhen)
prices.append(chaohai)
prices.append(chuangzhixinqu)
prices.append(darunfa)
prices.append(ershibazhong)
prices.append(huanxiu)
prices.append(hepingqu)
prices.append(jimozhoubian)
prices.append(jimobaolongchengshiguangchang)
prices.append(kaifaqu)
prices.append(lanseguigu)
prices.append(liantongdasha)
prices.append(mingduyuan)
prices.append(tongji)
prices.append(xinqichezhan)
prices.append(xiyuanzhuang)

hist = pygal.Bar(x_label_rotation=20, style=pygal.style.DarkStyle)

hist.title = "即墨市各分区平均平米单价"
hist.x_labels = ['鳌山卫镇', '潮海', '创智新区', '大润发', '二十八中', '环秀', '和平区',
                 '即墨周边', '即墨宝龙城市市场', '开发区', '蓝色硅谷', '联通大厦', '名都苑', '通济',
                 '新汽车站', '西元庄']

hist.y_title = "平均平米单价"

hist.add('分区', prices)
hist.render_to_file('即墨市各个分区平均单价.svg')
