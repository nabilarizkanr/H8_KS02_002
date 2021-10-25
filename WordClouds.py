import numpy as np
import pandas as pd
import xlrd
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image

alice_novel = open('alice_novel.txt', 'r').read()
alice_mask = np.array(Image.open('alice_mask.png'))
stopwords = set(STOPWORDS)

alice_wc = WordCloud(
    background_color='white',
    max_words=2000,
    mask=alice_mask,
    stopwords=stopwords
)
print(alice_wc.generate(alice_novel))
#Visualisasi
stopwords.add('said')
alice_wc.generate(alice_novel)
fig = plt.figure()
fig.set_figwidth(14)
fig.set_figheight(18)
plt.imshow(alice_mask, interpolation='bilinear')
plt.axis('off')
plt.show()