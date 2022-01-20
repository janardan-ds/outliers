#!/usr/bin/env python
# coding: utf-8

#                                            Janardan Pandey

# In[1]:


import warnings
warnings.filterwarnings("ignore")


# In[2]:


data=[11,10,12,14,15,10,11,107,12,13,15,16,14,109,14,15,12,10,11,12,14,112,16,14,15,15,14,13,12,105,10,121,150,12]


# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# ## Outliers using Z score :

# In[4]:


outliers=[]
def detect_outliers(d):
    threshold=1
    mean=np.mean(d)
    #print(mean)
    std=np.std(d)
    #print(std)
    
    for i in d:
        z_score=(i-mean)/std
        #print(z_score)
        if abs(z_score)>threshold:
            outliers.append(i)
    return outliers


# In[5]:


outliers_pt=detect_outliers(data)


# In[6]:


outliers_pt


# ## Outliers using IQR :
# 
# 
# 
# 

# In[7]:


import numpy as np
import pandas as pd
#d=[1,2,3,4,5,6,7,8,9]
#pd.DataFrame(d)


# In[8]:


Q1=np.percentile(data,25)
Q3=np.percentile(data,75)
print(Q1,Q3)


# In[9]:


IQR=Q3-Q1


# In[10]:


LB=Q1-(1.5*IQR)
UB=Q3+(1.5*IQR)


# In[11]:


print(LB,UB)


# In[12]:


l=[]
for j in data:
    if (j<LB or j>UB):
        l.append(j)
l


# ## Using BOXPLOT:

# In[13]:


h=[4,4.2,4.5,5.5,5.2,6.2,6.1,6.3,5.1,5.3,5.4,3.6,5.4,8.2,4.2,4.3,4.4,4.9,4.8,5.8,5.9,4.8]
d=[11,10,12,14,15,10,11,107,12,13,15,16,14,109,14,15,12,10,11,12,14,112]


# In[17]:


plt.boxplot(h)
plt.show()


# ## Using Scatter Plot

# In[18]:


plt.scatter(d,h)
plt.show()


# In[ ]:




