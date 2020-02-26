# DataSprints
Teste Técnico de Engenharia de Dados
#O projeto rodou via Jupyter Notebook
#Primeiramente tive de importar algumas bibliotecas para rodar o projeto.
```python
import pandas as pd
import json
import numpy as np
import datetime
import matplotlib.pyplot as plt
from collections import Counter
```
#Antes de importar os arquivos, tive de alterar a estrutura do json com as seguintes informações:
# {
#  "datas":[
#]}
#
#Importando o primeiro arquivo para o python
```python
with open('trips2009.json') as arq:    
    data = json.load(arq)
```

#Visualizando o arquivo
```python
print(data)
```

#Carregando os dados com o Pandas
```python
trips2009 = pd.DataFrame(data['datas'])
print(trips2009)
```

#Validando as colunas do arquivo
```python
trips2009.columns
```


```python
trips2009
```

#Verificando o tipamento de minhas colunas
```python
trips2009.dtypes
```


```python
trips2009.total_amount.mean()
```

#Adicionando no arquivo a coluna year
```python
trips2009_1 = trips2009.assign(year = '2009').copy(deep=True)
```


```python
trips2009_1
```

#realizando o mesmo processo de importação para o 2º arquivo com os dados de 2010
```python
with open('trips2010.json') as arq:
    data = json.load(arq)
trips2010 = pd.DataFrame(data['datas'])
trips2010_1 = trips2010.assign(year = '2010').copy(deep=True)
trips2010_1
```


```python
trips = trips2009_1.append(trips2010_1, ignore_index=True)
```


```python
trips.head(15)
```

#Criando um tratamento para importar os outros arquivos de forma mais rápida.
```python
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
```

#realizando o tratamento no 3° arquivo
```python
trips = trips.append(tratamento('trips2011.json','2011'), ignore_index=True)
```

#realizando o tratamento no 4º arquivo
```python
trips = trips.append(tratamento('trips2012.json','2012'), ignore_index=True)
```

#Verificando dados:
```python
trips.drop_duplicates()
trips.count()
```


```python
colunas_selecionadas = ["vendor_id","total_amount","fare_amount"]
trips[colunas_selecionadas].head()
```


```python
trips[  trips["total_amount"] == trips.total_amount.min() ]
```


```python
trips[  trips["total_amount"] == trips.total_amount.max() ]
```


```python
soma_media = trips.groupby("year")["total_amount"].sum()
soma_media
```


```python
%matplotlib notebook
soma_media.plot.pie()
```

#Qual a distância média percorrida por viagens com no máximo 2 passageiros;
```python
soma_trips2passengers = trips.groupby("passenger_count")["trip_distance"].sum()
soma_trips2passengers
```

```python
%matplotlib notebook
soma_trips2passengers.plot.pie()
```

#Quais os 3 maiores vendors em quantidade total de dinheiro arrecadado;
```python
top_tripsvendors = trips.groupby("vendor_id")["total_amount"].max()
top_tripsvendors
```


```python
%matplotlib notebook
top_tripsvendors.plot.barh()
```



#Tratando os dados de data, sendo mais especifico com mês, dia, ano e fim de semana
```python
trips["payment_type"]  = trips.payment_type.apply(lambda x :  str(x).lower())
trips["date_dropoff"]  = trips.dropoff_datetime.apply(lambda x :datetime.datetime.strptime(str(x).split('T')[0], "%Y-%m-%d") )
trips["day_dropoff"]   = trips.dropoff_datetime.apply(lambda x : datetime.datetime.strptime(str(x).split('T')[0], "%Y-%m-%d").day)  
trips["month_dropoff"] = trips.dropoff_datetime.apply(lambda x : datetime.datetime.strptime(str(x).split('T')[0], "%Y-%m-%d").month)
trips["year_dropoff"]  = trips.dropoff_datetime.apply(lambda x : datetime.datetime.strptime(str(x).split('T')[0], "%Y-%m-%d").year) 
trips["dayweek_dropoff"]  = trips.dropoff_datetime.apply(lambda x : datetime.datetime.strptime(str(x).split('T')[0], "%Y-%m-%d").weekday())

```

#Faça um histograma da distribuição mensal, nos 4 anos, de corridas pagas em dinheiro;
```python
aa = Counter(trips["month_dropoff"])

for a in sorted(Counter(trips["month_dropoff"])): 
    x = trips.loc[ (trips.payment_type == 'cash') & (trips.month_dropoff == a),"total_amount"]
    x.hist()
    #salva as imgs na pasta do projeto
    plt.savefig('histogram_'+str(a)+'.png')
    plt.close()
```

#Faça um gráfico de série temporal contando a quantidade de gorjetas de cada dia, nos
últimos 3 meses de 2012.
```python
limite = datetime.datetime.strptime("2012-10-01 00:00:00", "%Y-%m-%d %H:%M:%S")
tipA  = trips.loc[(pd.to_numeric(trips.month_dropoff) > 9) & (pd.to_numeric(trips.year_dropoff) == 2012),]
tipB      = Counter(tip_count.date_dropoff)
p.columns = ['date','count']
plt.plot(p['date'], p['count'])
plt.savefig('gorjeta.png')
plt.close()
```


```python

```
