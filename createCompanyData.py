
# coding: utf-8

# In[289]:




# In[13]:

import random
import pandas as pd
import numpy as np
import numpy.random as nr
from numpy import *


# In[27]:

#データセット①
x1 = 500 #
y1 = 1000 #データ幅の指定
zz = 3000 #出力データ個数(固定)
r1 = 0 #出力データの小数点指定(整数は０)


# In[28]:

#出力モデル
a = np.random.uniform(x1, y1, zz)
a = np.round(a, r1)
a


# In[29]:

#データセット②
x2 = 10000
y2 = 30000 #データ幅の指定
r2 = 0 #出力データの小数点指定(整数は０)


# In[30]:

b = np.random.uniform(x2, y2, zz)
b = np.round(b, r2)
b


# In[31]:

#データセット③
x3 = 1000
y3 = 2000 #データ幅の指定
r3 = 0 #出力データの小数点指定(整数は０)


# In[32]:

c = np.random.uniform(x3, y3, zz)
c = np.round(c, r3)
c


# In[33]:

#データセット④
x4 = 0
y4 = 1 #データ幅の指定
r4 = 0 #出力データの小数点指定(整数は０)


# In[34]:

d = np.random.uniform(x4, y4, zz)
d = np.round(d, r4)
d


# In[35]:

#時間設定
#開始時間,freqで時間幅を設定
#リファレンス http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases
dt = pd.date_range('2014-11-01 10:00', periods=zz, freq='2H30T17S')
dt


# In[36]:

#データセット⑤
wl = np.array(["パン","牛乳","お肉","お水","砂糖","お茶","野菜","菓子","果物","お米"])
wd = random.choice(wl, zz)
wd


# In[37]:

#index
index = np.arange(0,zz,1)
index


# In[40]:

#それぞれを統合
#各カラムの名前を設定
df = pd.DataFrame(
{'品物' : wd,
 '値段' : a,
 '販売数' : b})
df


# In[41]:

#CSVで出力
df.to_csv('output.csv', index=False)


# In[ ]:




# In[ ]:



