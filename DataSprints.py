
# coding: utf-8

# In[56]:

import pandas as pd
import json
import numpy as np
import datetime
import matplotlib.pyplot as plt
from collections import Counter


# In[57]:

with open('trips2009.json') as arq:    
    data = json.load(arq)


# In[58]:

print(data)


# In[59]:

trips2009 = pd.DataFrame(data['datas'])
print(trips2009)


# In[60]:

trips2009.columns


# In[61]:

trips2009


# In[62]:

trips2009.dtypes


# In[63]:

trips2009.total_amount.mean()


# In[64]:

trips2009_1 = trips2009.assign(year = '2009').copy(deep=True)


# In[65]:

trips2009_1


# In[66]:

with open('trips2010.json') as arq:
    data = json.load(arq)
trips2010 = pd.DataFrame(data['datas'])
trips2010_1 = trips2010.assign(year = '2010').copy(deep=True)
trips2010_1


# In[67]:

trips = trips2009_1.append(trips2010_1, ignore_index=True)


# In[68]:

trips.head(15)


# In[69]:

#Arquivo = trips2009.json
#yeartrip - 2009,2010,2011,2012

def tratamento(p1,p2):
    arquivo = p1
    yeartrip = p2
    with open(arquivo) as arq:
        data = json.load(arq)
    
        tripsA = pd.DataFrame(data['datas'])
        
        tripsB = tripsA.assign(year = yeartrip).copy(deep=True)
    
        return tripsB


# In[70]:

trips = trips.append(tratamento('trips2011.json','2011'), ignore_index=True)


# In[71]:

trips = trips.append(tratamento('trips2012.json','2012'), ignore_index=True)


# In[72]:

trips.drop_duplicates()
trips.count()


# In[73]:

colunas_selecionadas = ["vendor_id","total_amount","fare_amount"]
trips[colunas_selecionadas].head()


# In[74]:

trips[  trips["total_amount"] == trips.total_amount.min() ]


# In[75]:

trips[  trips["total_amount"] == trips.total_amount.max() ]


# In[76]:

soma_media = trips.groupby("year")["total_amount"].sum()
soma_media


# In[77]:

get_ipython().magic('matplotlib notebook')
soma_media.plot.pie()


# In[78]:

soma_trips2passengers = trips.groupby("passenger_count")["trip_distance"].sum()
soma_trips2passengers


# In[79]:

get_ipython().magic('matplotlib notebook')
soma_trips2passengers.plot.pie()


# In[80]:

top_tripsvendors = trips.groupby("vendor_id")["total_amount"].max()
top_tripsvendors


# In[81]:

get_ipython().magic('matplotlib notebook')
top_tripsvendors.plot.barh()


# In[82]:

cashtrips = trips.groupby("payment_type")["year"].count()
cashtrips


# In[83]:

colunas_cash = ["payment_type","year"]
trips[colunas_cash].head(20)


# In[84]:

trips["payment_type"]  = trips.payment_type.apply(lambda x :  str(x).lower())
trips["date_dropoff"]  = trips.dropoff_datetime.apply(lambda x :datetime.datetime.strptime(str(x).split('T')[0], "%Y-%m-%d") )
trips["day_dropoff"]   = trips.dropoff_datetime.apply(lambda x : datetime.datetime.strptime(str(x).split('T')[0], "%Y-%m-%d").day)  
trips["month_dropoff"] = trips.dropoff_datetime.apply(lambda x : datetime.datetime.strptime(str(x).split('T')[0], "%Y-%m-%d").month)
trips["year_dropoff"]  = trips.dropoff_datetime.apply(lambda x : datetime.datetime.strptime(str(x).split('T')[0], "%Y-%m-%d").year) 
trips["dayweek_dropoff"]  = trips.dropoff_datetime.apply(lambda x : datetime.datetime.strptime(str(x).split('T')[0], "%Y-%m-%d").weekday())


# In[85]:

aa = Counter(trips["month_dropoff"])

for a in sorted(Counter(trips["month_dropoff"])): 
    x = trips.loc[ (trips.payment_type == 'cash') & (trips.month_dropoff == a),"total_amount"]
    x.hist()
    #salva as imgs na pasta do projeto
    plt.savefig('histogram_'+str(a)+'.png')
    plt.close()


# In[86]:

limite = datetime.datetime.strptime("2012-10-01 00:00:00", "%Y-%m-%d %H:%M:%S")
tipA  = trips.loc[(pd.to_numeric(trips.month_dropoff) > 9) & (pd.to_numeric(trips.year_dropoff) == 2012),]
tipB      = Counter(tip_count.date_dropoff)
p.columns = ['date','count']
plt.plot(p['date'], p['count'])
plt.savefig('gorjeta.png')
plt.close()


# In[ ]:



