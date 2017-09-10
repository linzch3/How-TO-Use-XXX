# -*- coding: utf-8 -*-
"""
演示程序：读入一个txt文件（英文小说月亮与六便士），取其中的词汇生成一张词云图
"""

# 导入 wordcloud 模块和 matplotlib 模块
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# 读入一个txt文件

with open('TheMoonAndSixpence.txt','r',encoding='utf-8') as f:
    text=f.read()
# 生成词云
wordcloud = WordCloud().generate(text)

# 显示词云图片
plt.figure(num="demo", figsize=(5, 6),dpi=500, facecolor='w',edgecolor='w')
plt.axis('off')
plt.imshow(wordcloud)
plt.show()
# 保存图片
wordcloud.to_file('outputFiles/demo2_output.jpg')
plt.close()

