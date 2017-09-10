# -*- coding: utf-8 -*-
"""
演示程序：读入一个txt文件（英文小说月亮与六便士），取其中的词汇生成一张词云图
"""

# 导入 wordcloud 模块和 matplotlib 模块
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
from numpy import array
bg_pic= array(Image.open('pictures/alice.png'))
plt.imshow(bg_pic)
plt.axis('off')
plt.show()
# 配置词云参数
wc = WordCloud(
    # 设置字体
    font_path = 'simhei.ttf',
    # 设置背景色
    background_color='white',
    # 允许最大词汇
    max_words=200,
    # 词云形状
    mask=bg_pic,
    # 最大号字体
    max_font_size=100,
)

with open('TheMoonAndSixpence.txt','r',encoding='utf-8') as f:
    text=f.read()
# 生成词云
wordcloud = wc.generate(text)

# 显示词云图片
plt.figure(num="demo", figsize=(5, 6),dpi=50000, facecolor='w',edgecolor='w')
plt.axis('off')
plt.imshow(wordcloud)
plt.show()
# 保存图片
wordcloud.to_file('outputFiles/demo3_output.jpg')
plt.close()

