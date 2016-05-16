#!/usr/bin/env python
# coding: utf-8

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys

reload(sys)
sys.setdefaultencoding('utf-8')   
custom_font = mpl.font_manager.FontProperties(fname='/usr/share/fonts/goffer.ttf')

font_size = 10 # 字体大小
fig_size = (9, 6) # 图表大小

names = (u'os1', u'os2')   # 对比OS名称
subjects = (u'type1', u'type2', u'type3') # 对比项目
scores = ((65, 90, 75), (85, 80, 90)) # 项目数值

# 更新字体大小
mpl.rcParams['font.size'] = font_size
# 更新图表大小
mpl.rcParams['figure.figsize'] = fig_size
# 设置柱形图宽度
bar_width = 0.35

index = np.arange(len(scores[0]))
# 绘制「OS1」的结果
rects1 = plt.bar(index, scores[0], bar_width, color='#800080', label=names[0])
# 绘制「OS2」的结果
rects2 = plt.bar(index + bar_width, scores[1], bar_width, color='#4682B4', label=names[1])
# X轴标题
plt.xticks(index + bar_width, subjects, fontproperties=custom_font)
# Y轴范围
plt.ylim(ymax=100, ymin=0)
# 图表标题
plt.title(u'test result', fontproperties=custom_font)
# 图例显示在图表下方
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.035), fancybox=True, ncol=3, prop=custom_font)

# 添加数据标签
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 3, height, height, ha='center', va='bottom')
        # 柱形图边缘用白色填充，纯粹为了美观
        rect.set_edgecolor('blue')

add_labels(rects1)
add_labels(rects2)

# 图表输出到本地
plt.savefig('scores_par.png')
