#!/usr/bin/env python
# coding: utf-8

# In[66]:


import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import numpy as np
from pandas.plotting import scatter_matrix
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
start = datetime.datetime(2020,1,1)
end = datetime.datetime(2020,12,11)


# In[2]:


moderna = web.DataReader("MRNA", 'yahoo',start,end)
pfizer = web.DataReader("PFE", 'yahoo',start,end)
biontech = web.DataReader("BNTX", 'yahoo',start,end)


# In[5]:


moderna.head()


# In[7]:


pfizer.head()


# In[6]:


biontech.head()


# In[18]:


moderna['Open'].plot(label='Moderna',figsize=(15,7))
pfizer['Open'].plot(label='Pfizer')
biontech['Open'].plot(label='BioNTech')
plt.ylabel('Opening Stock Price')
plt.title('Opening Stock Prices of Moderna, Pfizer and BioNTech')
plt.legend()


# In[17]:


moderna['Close'].plot(label='Moderna',figsize=(15,7))
pfizer['Close'].plot(label='Pfizer')
biontech['Close'].plot(label='BioNTech')
plt.ylabel('Closing Stock Price')
plt.title('Closing Stock Prices of Moderna, Pfizer and BioNTech')
plt.legend()


# In[16]:


moderna['Open'].plot(label='Moderna',figsize=(15,7))
pfizer['Open'].plot(label='Pfizer')
biontech['Open'].plot(label='BioNTech')
plt.ylabel('Stock Prices')
plt.title('Opening and Closing Stock Prices of Moderna, Pfizer and BioNTech')
plt.legend()
moderna['Close'].plot(label='Moderna',figsize=(15,7))
pfizer['Close'].plot(label='Pfizer')
biontech['Close'].plot(label='BioNTech')


# In[19]:


moderna['Volume'].plot(label='Moderna',figsize=(15,7))
pfizer['Volume'].plot(label='Pfizer',figsize=(15,7))
biontech['Volume'].plot(label='BioNTech',figsize=(15,7))
plt.ylabel('Volume Traded')
plt.title('Volume of stock traded for Moderna, Pfizer and BioNTech')
plt.legend()


# In[21]:


pfizer.iloc[[pfizer['Volume'].argmax()]]


# In[55]:


pfizer.iloc[210:250]['Open'].plot(figsize=(15,7))


# In[57]:


moderna['Total Traded'] = moderna['Open'] * moderna['Volume']
pfizer['Total Traded'] = pfizer['Open'] * pfizer['Volume']
biontech['Total Traded'] = biontech['Open'] * biontech['Volume']


# In[58]:


moderna['Total Traded'].plot(label='moderna',figsize = (15,7))
pfizer['Total Traded'].plot(label='pfizer',figsize = (15,7))
biontech['Total Traded'].plot(label='biontech',figsize = (15,7))
plt.legend()
plt.ylabel('Total Traded')


# In[59]:


moderna['Total Traded'].argmax()


# In[60]:


moderna.iloc[[moderna['Total Traded'].argmax()]]


# In[64]:


pfizer['Open'].plot(label = 'No moving Average', figsize=(15,7))
pfizer['MA20'] = pfizer['Open'].rolling(20).mean()
pfizer['MA20'].plot(label='MA50')
plt.legend()


# In[67]:


drug_comp = pd.concat([moderna['Open'],pfizer['Open'],biontech['Open']], axis = 1)
drug_comp.columns = ['Moderna Open', 'Pfizer Open', 'BioNTech Open']


# In[68]:


scatter_matrix(drug_comp,figsize=(8,8), hist_kwds={'bins':50})

