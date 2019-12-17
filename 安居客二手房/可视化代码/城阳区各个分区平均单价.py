import json
import pygal

filename = '城阳区清洗后.json'
with open(filename) as f:
    datas = json.load(f)

chengyangbaolong = 0
chengyangbaolongnum = 0
chengyangzhoubian = 0
chengyangzhoubiannum = 0
guoxuegongyuan = 0
guoxuegongyuannum = 0
gaoxinqu = 0
gaoxinqunum = 0
hongdao = 0
hongdaonum = 0
hetao = 0
hetaonum =0
jiajiayuan = 0
jiajiayuannum = 0
liuting = 0
liutingnum = 0
nongyedaxue = 0
nongyedaxuenum = 0
quzhengfu = 0
quzhengfunum = 0
shangma = 0
shangmanum = 0
shiyanerxiao = 0
shiyanerxiaonum = 0
shijigongyuan = 0
shijigongyuannum = 0
tiantaicheng = 0
tiantaichengnum = 0
xiazhuang = 0
xiazhuangnum = 0
xifuzhen = 0
xifuzhennum = 0

for data in datas:
    if data['地址'] == '城阳宝龙城市广场':
        chengyangbaolong += data['平米单价']
        chengyangbaolongnum += 1
    elif data['地址'] == '城阳周边':
        chengyangzhoubian += data['平米单价']
        chengyangzhoubiannum += 1
    elif data['地址'] == '国学公园':
        guoxuegongyuan += data['平米单价']
        guoxuegongyuannum += 1
    elif data['地址'] == '高新区':
        gaoxinqu += data['平米单价']
        gaoxinqunum += 1
    elif data['地址'] == '红岛':
        hongdao += data['平米单价']
        hongdaonum += 1
    elif data['地址'] == '河套':
        hetao += data['平米单价']
        hetaonum += 1
    elif data['地址'] == '家佳源':
        jiajiayuan += data['平米单价']
        jiajiayuannum += 1
    elif data['地址'] == '流亭':
        liuting += data['平米单价']
        liutingnum += 1
    elif data['地址'] == '农业大学':
        nongyedaxue += data['平米单价']
        nongyedaxuenum += 1
    elif data['地址'] == '区政府':
        quzhengfu += data['平米单价']
        quzhengfunum += 1
    elif data['地址'] == '上马':
        shangma += data['平米单价']
        shangmanum += 1
    elif data['地址'] == '实验二小':
        shiyanerxiao += data['平米单价']
        shiyanerxiaonum += 1
    elif data['地址'] == '世纪公园':
        shijigongyuan += data['平米单价']
        shijigongyuannum += 1
    elif data['地址'] == '天泰城':
        tiantaicheng += data['平米单价']
        tiantaichengnum += 1
    elif data['地址'] == '夏庄':
        xiazhuang += data['平米单价']
        xiazhuangnum += 1
    elif data['地址'] == '惜福镇':
        xifuzhen += data['平米单价']
        xifuzhennum += 1

chengyangbaolong /= chengyangbaolongnum
chengyangzhoubian /= chengyangzhoubiannum
guoxuegongyuan /= guoxuegongyuannum
gaoxinqu /= gaoxinqunum
hongdao /= hongdaonum
hetao /= hetaonum
jiajiayuan /= jiajiayuannum
liuting /= liutingnum
nongyedaxue /= nongyedaxuenum
quzhengfu /= quzhengfunum
shangma /= shangmanum
shiyanerxiao /= shiyanerxiaonum
shijigongyuan /= shijigongyuannum
tiantaicheng /= tiantaichengnum
xiazhuang /= xiazhuangnum
xifuzhen /= xifuzhennum

average_price = []
average_price.append(chengyangbaolong)
average_price.append(chengyangzhoubian)
average_price.append(guoxuegongyuan)
average_price.append(gaoxinqu)
average_price.append(hongdao)
average_price.append(hetao)
average_price.append(jiajiayuan)
average_price.append(liuting)
average_price.append(nongyedaxue)
average_price.append(quzhengfu)
average_price.append(shangma)
average_price.append(shiyanerxiao)
average_price.append(shijigongyuan)
average_price.append(tiantaicheng)
average_price.append(xiazhuang)
average_price.append(xifuzhen)

hist = pygal.Bar(x_label_rotation=40, style=pygal.style.DarkStyle)

hist.title = "城阳区各个分区平均平米单价"
hist.x_labels = ['城阳宝龙城市广场', '城阳周边', '国学公园', '高新区', '红岛', '河套',
                 '家佳源', '流亭', '农业大学', '区政府', '上马', '实验二小',
                 '世纪公园', '天泰城', '夏庄', '惜福镇',]
# hist.x_title = '分区'
hist.y_title = "平均平米单价"

hist.add("分区", average_price)
hist.render_to_file('城阳区各个分区平均平米单价.svg')
