# -*- coding: utf-8 -*-
"""
演示程序：结合tuple和函数generate_from_frequencies，生成一张词云图
"""

# 导入 wordcloud 模块和 matplotlib 模块
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读入一组词频字典文件
text_dict = (
    ('you', 3000),
    ('love', 3500),
    ('I', 3000),
    ('Li', 2800),
    ('Phone', 3000),
    ('my',300),
    ('mu~',2000),
    ('mu~~',510),
    ('heart',500),
    ('sweet',180)
)
# 生成词云
wc=WordCloud()
wordcloud = wc.generate_from_frequencies(frequencies=text_dict)
# 显示词云图片
plt.figure(num="demo", figsize=(5, 6),dpi=500, facecolor='w',edgecolor='w')
plt.axis('off')
plt.imshow(wordcloud)
plt.show()
# 保存图片
wc.to_file('outputFiles/demo1_output.jpg')
plt.close()

