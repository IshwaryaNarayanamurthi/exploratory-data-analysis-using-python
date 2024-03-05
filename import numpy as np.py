import numpy as np
import pandas as pd
df_can = pd.read_csv('Canada.csv')
print('Data read into a pandas dataframe!')
df_can.head(5)
df_can.set_index('Country',inplace=True)
df_can.head(5)
years = list(map(str, range(1980, 2014)))


import matplotlib as mpl
import matplotlib.pyplot as plt
print('Matplotlib version: ', mpl.__version__)  # >= 2.0.0
print(plt.style.available)
mpl.style.use(['ggplot'])
year=list(map(str,range(1980,2014)))
df_CI=df_can.loc[['India','China'],year]
df_CI.head()
df_CI.plot(kind='line')
df_CI = df_CI.transpose()
df_CI.head()
df_CI.index=df_CI.index.map(int)
df_CI.plot(kind='line')
plt.title('Immigration')
plt.xlabel('Years')
plt.ylabel('Number of Immigrants')
plt.show()
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
df_top5=df_can.head(5)
df_top5=df_top5[years].transpose()
print(df_top5)
df_top5.index = df_top5.index.map(int) 
df_top5.plot(kind='line', figsize=(14, 8)) 


plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')


plt.show()