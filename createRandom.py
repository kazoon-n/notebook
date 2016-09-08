
# coding: utf-8

# In[1]:




# In[2]:

import random
import pandas as pd
import numpy as np


# In[3]:

#データセット①
x1 = 10 #
y1 = 20 #データ幅の指定
zz = 3000 #出力データ個数(固定)
r1 = 2 #出力データの小数点指定(整数は０)


# In[4]:

#出力モデル
a = np.random.uniform(x1, y1, zz)
a = np.round(a, r1)
a


# In[5]:

#データセット②
x2 = 0.005
y2 = 0.1 #データ幅の指定
r2 = 4 #出力データの小数点指定(整数は０)


# In[6]:

b = np.random.uniform(x2, y2, zz)
b = np.round(b, r2)
b


# In[7]:

#データセット③
x3 = 1000
y3 = 2000 #データ幅の指定
r3 = 3 #出力データの小数点指定(整数は０)


# In[8]:

c = np.random.uniform(x3, y3, zz)
c = np.round(c, r3)
c


# In[9]:

#データセット④
x4 = 0
y4 = 1 #データ幅の指定
r4 = 0 #出力データの小数点指定(整数は０)


# In[10]:

d = np.random.uniform(x4, y4, zz)
d = np.round(d, r4)
d


# In[11]:

#時間設定
#開始時間,freqで時間幅を設定
#リファレンス http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases
dt = pd.date_range('2014-11-01 10:00', periods=zz, freq='2H30T17S')
dt


# In[12]:

#index
index = np.arange(0,zz,1)
index


# In[13]:

#それぞれを統合
#各カラムの名前を設定
df = pd.DataFrame(
{'index' : index,
 '時間' : dt,
 'センサー１' : a,
 'センサー２' : b,
 'センサー３' : c,
 'センサー４' : d})
df


# In[14]:

#CSVで出力
df.to_csv('output.csv', index=False)


# In[ ]:




# In[ ]:



