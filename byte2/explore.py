
# coding: utf-8

# In[9]:


import csv
import httplib2
from apiclient.discovery import build
import urllib
import json


# This API key is provided by google as described in the tutorial
API_KEY = 'AIzaSyD6dPrUdI_UAlyF-H09oltdT_S-mvVnt4o'

# This is the table id for the fusion table
TABLE_ID = '1-fFaNY4vYfMCqRe74Mx23qFJvq1dND_AVSYfY0C2'

try:
    fp = open("dat.json")
    response = json.load(fp)
except IOError:
    service = build('fusiontables', 'v1', developerKey=API_KEY)
    query = "SELECT * FROM " + TABLE_ID
    response = service.query().sql(sql=query).execute()
    fp = open("dat.json", "w+")
    json.dump(response, fp)


# In[10]:


print len(response['rows'])


# In[11]:


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


# In[12]:


data_df = pd.DataFrame(response[u'rows'], columns = response[u'columns'])


# In[13]:


data_df.head()


# In[24]:


x = data_df['fatalities_85_99']
y = data_df['fatalities_00_14']


# In[17]:


x


# In[43]:


plt.scatter(x,y)
plt.axis([-10, 600, -10, 600])
plt.xlabel('1985-1999')
plt.ylabel('2000-2014')
plt.suptitle('Total Number of Fatalities')
plt.show()
plt.savefig('fatalities.png')


# In[46]:


x2 = data_df['incidents_85_99']
y2 = data_df['incidents_00_14']
plt.scatter(x2,y2)
plt.axis([-1, 80, -1, 80])
plt.xlabel('1985-1999')
plt.ylabel('2000-2014')
plt.suptitle('Total Number of Incidents')
plt.show()
plt.savefig('incidents.png')


# In[60]:


ask = []
for i in data_df['avail_seat_km_per_week']:
  ask.append(float(i)*782.143 / 1000000000000)


# In[63]:


x3=[]
for i in range(len(data_df['fatalities_85_99'])):
  a=float(data_df['fatalities_85_99'][i])/ask[i]
  x3.append(a)


# In[64]:


y3=[]
for i in range(len(data_df['fatalities_00_14'])):
  a=float(data_df['fatalities_00_14'][i])/ask[i]
  y3.append(a)


# In[68]:


plt.scatter(x3,y3)
plt.axis([-10, 1400, -10, 1400])
plt.xlabel('1985-1999')
plt.ylabel('2000-2014')
plt.suptitle('Number of Fatalities per 1 Trillion Seat Kilometers')
plt.show()
plt.savefig('fatalitiesperask.png')


# In[69]:


x4=[]
for i in range(len(data_df['incidents_85_99'])):
  a=float(data_df['incidents_85_99'][i])/ask[i]
  x4.append(a)


# In[70]:


y4=[]
for i in range(len(data_df['incidents_00_14'])):
  a=float(data_df['incidents_00_14'][i])/ask[i]
  y4.append(a)


# In[72]:


plt.scatter(x4,y4)
plt.axis([-1, 100, -1, 100])
plt.xlabel('1985-1999')
plt.ylabel('2000-2014')
plt.suptitle('Number of Incidents per 1 Trillion Seat Kilometers')
plt.show()
plt.savefig('incidentsperask.png')
