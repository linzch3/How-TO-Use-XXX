#-*- coding:utf-8 -*-
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
from collections import Counter
from numpy import array
# 读入 西游记 txt 文件，windows 下过滤编码错误
with open('月亮与六便士.txt',encoding='utf-8') as f:
    texts=f.read()
# 使用 jieba 分词
text_jieba = list(jieba.cut(texts))

text=[]
for t in text_jieba:
    if not len(t)<=1:
        text.append(t)
c = Counter(text)

# 使用 counter 做词频统计，选取出现频率前 100 的词汇
common_c = c.most_common(100)
#"""
# 读入图片
bg_pic= array(Image.open('pictures/alice.png'))
# 配置词云参数
wc = WordCloud(
    # 设置字体
    font_path = 'simhei.ttf',
    # 设置背景色
    background_color='white',
    # 允许最大词汇
    max_words=200,
    # 词云形状
    #mask=bg_pic,
    # 最大号字体
    max_font_size=100,
)
# 显示词云图片
plt.figure(num="demo", figsize=(10, 6),dpi=500, facecolor='w',edgecolor='w')
# 生成词云
wc.generate_from_frequencies(tuple(common_c))
# 生成图片并显示
plt.figure()
plt.imshow(wc)
plt.axis('off')
plt.show()
# 保存图片
wc.to_file('outputFiles/demo4_1_output.jpg')
plt.close()