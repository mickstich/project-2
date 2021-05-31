#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
pd.set_option('display.max_colwidth', 100)

import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

import warnings
warnings.filterwarnings("ignore")


# In[6]:


a=pd.read_csv("E:\youtube.csv")
c=a.drop(["Unnamed: 1","Unnamed: 4","Unnamed: 5","Unnamed: 6","ExportComments.com","Unnamed: 8"],axis=1)

d=c.set_axis(["Name", "Time", "message"], axis=1)
g=[] 
for i in d.message.values:
    try:
        analysis =TextBlob(i)
        g.append(analysis.sentiment.polarity)
        
    except:
        g.append(0)
d['g']=g
neutral=d['g'][d.g==0]= 0
positive=d['g'][d.g > 0]= 1
negative=d['g'][d.g < 0]= -1

positive = d[d.g==1]
positive.head(10)


# In[7]:


negative = d[d.g==-1]
negative.head(10)


# In[8]:


neutral = d[d.g==0]
neutral.head(10)


# In[ ]:


d.g.value_counts().plot.bar()

