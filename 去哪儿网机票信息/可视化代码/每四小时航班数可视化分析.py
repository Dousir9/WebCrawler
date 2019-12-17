import json
import pygal

filename = "每四小时航班数.json"

with open(filename) as f:
    datas = json.load(f)

date = []
for data in datas:
    for key in data.items():
        date.append(key[0])

number = []
for data in datas:
    for key in data.items():
        if key[0] == date[0]:
            number.append(key[1])
        elif key[0] == date[1]:
            number.append(key[1])
        elif key[0] == date[2]:
            number.append(key[1])
        elif key[0] == date[3]:
            number.append(key[1])
        elif key[0] == date[4]:
            number.append(key[1])
        elif key[0] == date[5]:
            number.append(key[1])
        elif key[0] == date[6]:
            number.append(key[1])
        elif key[0] == date[7]:
            number.append(key[1])
        elif key[0] == date[8]:
            number.append(key[1])
        elif key[0] == date[9]:
            number.append(key[1])
        elif key[0] == date[10]:
            number.append(key[1])
        elif key[0] == date[11]:
            number.append(key[1])
        elif key[0] == date[12]:
            number.append(key[1])
        elif key[0] == date[13]:
            number.append(key[1])
        elif key[0] == date[14]:
            number.append(key[1])
        elif key[0] == date[15]:
            number.append(key[1])
        elif key[0] == date[16]:
            number.append(key[1])
        elif key[0] == date[17]:
            number.append(key[1])
        elif key[0] == date[18]:
            number.append(key[1])
        elif key[0] == date[19]:
            number.append(key[1])
        elif key[0] == date[20]:
            number.append(key[1])
        elif key[0] == date[21]:
            number.append(key[1])
        elif key[0] == date[22]:
            number.append(key[1])
        elif key[0] == date[23]:
            number.append(key[1])
        elif key[0] == date[24]:
            number.append(key[1])
        elif key[0] == date[25]:
            number.append(key[1])
        elif key[0] == date[26]:
            number.append(key[1])
        elif key[0] == date[27]:
            number.append(key[1])
        elif key[0] == date[28]:
            number.append(key[1])
        elif key[0] == date[29]:
            number.append(key[1])
        elif key[0] == date[30]:
            number.append(key[1])
        elif key[0] == date[31]:
            number.append(key[1])
        elif key[0] == date[32]:
            number.append(key[1])
        elif key[0] == date[33]:
            number.append(key[1])
        elif key[0] == date[34]:
            number.append(key[1])
        elif key[0] == date[35]:
            number.append(key[1])
        elif key[0] == date[36]:
            number.append(key[1])
        elif key[0] == date[37]:
            number.append(key[1])
        elif key[0] == date[38]:
            number.append(key[1])
        elif key[0] == date[39]:
            number.append(key[1])
        elif key[0] == date[40]:
            number.append(key[1])
        elif key[0] == date[41]:
            number.append(key[1])
        elif key[0] == date[42]:
            number.append(key[1])
        elif key[0] == date[43]:
            number.append(key[1])
        elif key[0] == date[44]:
            number.append(key[1])
        elif key[0] == date[45]:
            number.append(key[1])
        elif key[0] == date[46]:
            number.append(key[1])
        elif key[0] == date[47]:
            number.append(key[1])
        elif key[0] == date[48]:
            number.append(key[1])
        elif key[0] == date[49]:
            number.append(key[1])
        elif key[0] == date[50]:
            number.append(key[1])
        elif key[0] == date[51]:
            number.append(key[1])
        elif key[0] == date[52]:
            number.append(key[1])
        elif key[0] == date[53]:
            number.append(key[1])
        elif key[0] == date[54]:
            number.append(key[1])
        elif key[0] == date[55]:
            number.append(key[1])
        elif key[0] == date[56]:
            number.append(key[1])
        elif key[0] == date[57]:
            number.append(key[1])
        elif key[0] == date[58]:
            number.append(key[1])
        elif key[0] == date[59]:
            number.append(key[1])
        elif key[0] == date[60]:
            number.append(key[1])
        elif key[0] == date[61]:
            number.append(key[1])
        elif key[0] == date[62]:
            number.append(key[1])
        elif key[0] == date[63]:
            number.append(key[1])
        elif key[0] == date[64]:
            number.append(key[1])
        elif key[0] == date[65]:
            number.append(key[1])
        elif key[0] == date[66]:
            number.append(key[1])
        elif key[0] == date[67]:
            number.append(key[1])
        elif key[0] == date[68]:
            number.append(key[1])
        elif key[0] == date[69]:
            number.append(key[1])
        elif key[0] == date[70]:
            number.append(key[1])
        elif key[0] == date[71]:
            number.append(key[1])
        elif key[0] == date[72]:
            number.append(key[1])
        elif key[0] == date[73]:
            number.append(key[1])
        elif key[0] == date[74]:
            number.append(key[1])
        elif key[0] == date[75]:
            number.append(key[1])
        elif key[0] == date[76]:
            number.append(key[1])
        elif key[0] == date[77]:
            number.append(key[1])
        elif key[0] == date[78]:
            number.append(key[1])
        elif key[0] == date[79]:
            number.append(key[1])
        elif key[0] == date[80]:
            number.append(key[1])
        elif key[0] == date[81]:
            number.append(key[1])
        elif key[0] == date[82]:
            number.append(key[1])
        elif key[0] == date[83]:
            number.append(key[1])
        elif key[0] == date[84]:
            number.append(key[1])
        elif key[0] == date[85]:
            number.append(key[1])
        elif key[0] == date[86]:
            number.append(key[1])
        elif key[0] == date[87]:
            number.append(key[1])
        elif key[0] == date[88]:
            number.append(key[1])
        elif key[0] == date[89]:
            number.append(key[1])
        elif key[0] == date[90]:
            number.append(key[1])
        elif key[0] == date[91]:
            number.append(key[1])
        elif key[0] == date[92]:
            number.append(key[1])
        elif key[0] == date[93]:
            number.append(key[1])
        elif key[0] == date[94]:
            number.append(key[1])
        elif key[0] == date[95]:
            number.append(key[1])
        elif key[0] == date[96]:
            number.append(key[1])
        elif key[0] == date[97]:
            number.append(key[1])
        elif key[0] == date[98]:
            number.append(key[1])
        elif key[0] == date[99]:
            number.append(key[1])
        elif key[0] == date[100]:
            number.append(key[1])
        elif key[0] == date[101]:
            number.append(key[1])
        elif key[0] == date[102]:
            number.append(key[1])
        elif key[0] == date[103]:
            number.append(key[1])
        elif key[0] == date[104]:
            number.append(key[1])
        elif key[0] == date[105]:
            number.append(key[1])
        elif key[0] == date[106]:
            number.append(key[1])
        elif key[0] == date[107]:
            number.append(key[1])
        elif key[0] == date[108]:
            number.append(key[1])
        elif key[0] == date[109]:
            number.append(key[1])
        elif key[0] == date[110]:
            number.append(key[1])
        elif key[0] == date[111]:
            number.append(key[1])
        elif key[0] == date[112]:
            number.append(key[1])
        elif key[0] == date[113]:
            number.append(key[1])
        elif key[0] == date[114]:
            number.append(key[1])
        elif key[0] == date[115]:
            number.append(key[1])
        elif key[0] == date[116]:
            number.append(key[1])
        elif key[0] == date[117]:
            number.append(key[1])
        elif key[0] == date[118]:
            number.append(key[1])
        elif key[0] == date[119]:
            number.append(key[1])
        elif key[0] == date[120]:
            number.append(key[1])

time = [
    '11-18','','','','','','11-19','','','','','','11-20','','','','','','11-21','','','','','',
    '11-22','','','','','','11-23','','','','','','11-24','','','','','','11-25','','','','','',
    '11-26','','','','','','11-27','','','','','','11-28','','','','','','12-29','','','','','',
    '12-30','','','','','','12-01','','','','','','12-02','','','','','','12-03','','','','','',
    '12-04','','','','','','12-05','','','','','','12-06','','','','','','12-07','','','','','',
]
print(number)
line_chart = pygal.Line(x_label_rotation = 80)
# style=pygal.style.DarkStyle
line_chart.title = "青岛至北京20天每四小时航班数"
line_chart.x_labels = time

line_chart.add('', number)



line_chart.render_to_file("青岛至北京20天每四小时航班数.svg")



