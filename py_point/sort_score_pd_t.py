import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

'''
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 25)
'''


df = pd.read_excel(r'C:\Users\Administrator\1.xls')
df['rank'] = df['score'].rank(method='min', ascending=False)

def le_100(x):
    return 5000 - (x - 1) * 6

def le_200(x):
    return le_100(100) - (x - 100) * 5

def le_300(x):
    return le_200(200) - (x - 200) * 4

def le_500(x):
    return le_300(300) - (x - 300) * 3

def le_800(x):
    return le_500(500) - (x - 500) * 2

def gt_800(x):
    return le_800(800) - (x - 800) * 1

def get_point(x):
    if x > 0:
        if x <= 100:
            return le_100(x)
        elif x <= 200:
            return le_200(x)
        elif x <= 300:
            return le_300(x)
        elif x <= 500:
            return le_500(x)
        elif x <= 800:
            return le_800(x)
        elif x > 800:
            return gt_800(x)
    else:
        return

df['point'] = df['rank'].apply(get_point)

df.sort_values(['class','score'],ascending=[1,0],inplace=True)
grouped_A = df[df['class'].isin([316,315,314,321,320,319])].groupby(['class']).head(70)
#print(grouped_A)
grouped_B = df[df['class'].isin([310,311,307,308,309,325, 326, 327, 328])].groupby(['class']).head(60)

#class_217 = df[df['class'] == 217]
#print(class_217['point'].mean())

grouped = pd.concat([grouped_A, grouped_B])
#print(grouped.groupby('class').mean().sort_values(by='point', ascending=False))

#print(df['point'].__class__)

#print(df.groupby('class').mean().sort_values(by='point', ascending=False))
#print(grouped.groupby('class').count())
#print(df.groupby('class').count())
result = grouped.groupby('class').mean().sort_values(by='point', ascending=False)
count = grouped.groupby('class').count()['name']
#result = pd.merge(res, count, on='class',how='inner')

result = result.apply(lambda x: round(x, 4))
dict_result = result.to_dict()['point']
result['count'] = count
print(count)
print(result)
'''
ind = np.arange(len(result['point']))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, result['point'], width, label = 'Point')
rects2 = ax.bar(ind - width/2, result['count'], width, label = 'Count')
ax.set_ylabel('Points')
ax.set_title('Point of each class')
ax.set_xticks(ind)
ax.set_xticklabels(result['point'].index)
ax.legend()
#result['point'].plot(kind='bar')

fig,ax=plt.subplots()

ax.bar(result.index,result["point"])
ax.set_xlabel("Class")  #设置x轴标签
ax.set_ylabel("Point")  #设置y轴标签
ax.set_title("Point of each class")  #设置标题
ax.set_xlim(200, 240)  #设置x轴数据限值


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
autolabel(rects2, "right")

plt.show()
'''

