import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('Womens softlines E-commerce Dataset.csv')
print(df.head(10))
print(df.tail(10))
print(df.describe())
df.drop(['Unnamed: 0','Title','Review Text','Unnamed: 11','Unnamed: 12','Positive Feedback Count' ], axis='columns', inplace=True)
print(df.head())
duplicate_rows = df[df.duplicated()]
df.drop_duplicates(inplace=True)
df.rename(columns={'Recommended IND':'Recommended',   
                   'Division Name':'Division', 'Department Name':'Department', 
                   'Class Name ':' Product name'}, inplace=True)
print(df.columns)
print(df.shape)
print(df["Age"].value_counts())
print(df["Rating"].value_counts())
print(df["Division"].value_counts())
print(df["Department"].value_counts())
print(df[' Product name'].value_counts())
print(df["Recommended"].value_counts())
plt.figure(figsize=(20, 8))
plt.title('Customer Age Distribution', fontsize=30)
plt.xlabel("Age", fontsize=24)
plt.ylabel("The Number of Customers", fontsize=18)
sns.histplot(data=df, x='Age', kde=True, bins=50)
plt.show()
fig = plt.figure(figsize=(14, 14))
ax1 = plt.subplot2grid((2, 2), (0, 0))
ax1 = plt.xticks(rotation=45)
ax1 = sns.countplot(df['Division'])
plt.xlabel('Division',fontsize=10,fontweight="bold")
plt.ylabel("Counts Division Clothes", fontsize=10)
ax1 = plt.title("Numbers Division Women Clothes",fontweight="bold",fontsize=10)
plt.show()
fig = plt.figure(figsize=(14, 14))
ax1 = plt.subplot2grid((2, 2), (0, 0))
ax1 = plt.xticks(rotation=45)
ax1 = sns.countplot(df['Division'])
plt.xlabel('Division',fontsize=10,fontweight="bold")
plt.ylabel("Counts Division Clothes", fontsize=10 ,fontweight="bold")
ax1 = plt.title("Numbers Division Women Clothes",fontweight="bold",fontsize=10)
plt.show()

ax2 = plt.subplot2grid((2, 2), (0, 1))
ax2 = plt.xticks(rotation=45)
ax2 = sns.countplot(df['Department'])
plt.xlabel('Department',fontsize=10,fontweight="bold")
plt.ylabel("Counts Department Clothes", fontsize=10 ,fontweight="bold")
ax2 = plt.title("Numbers Departments Women Clothes",fontweight="bold",fontsize=10)
plt.show()


ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)
ax3 = plt.xticks(rotation=45)
ax3 = sns.countplot(df[' Product name'])
plt.xlabel(' Product name',fontsize=10,fontweight="bold")
plt.ylabel("Counts Product Clothes", fontsize=10 ,fontweight="bold")
ax3 = plt.title("Numbers Product name",fontweight="bold",fontsize=10)
plt.show()
data_Rating=df.groupby(' Product name')[['Rating']].mean().sort_values(['Rating'],ascending=False).reset_index()
data_Rating.sort_values(['Rating'])
plt.figure(figsize=(10,10))
plt.xticks(rotation=90)
# make ScatterPlot to show Relationship between age and Product nam
sns.barplot(x=' Product name', y="Rating", data=data_Rating)
# set labels
plt.xlabel("Clothes names ",size=15 ,weight = 'bold')
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],['Intimates', 'Dresses', 'Pants', 'Blouses', 'Knits', 'Outerwear',
       'Lounge', 'Sweaters', 'Skirts', 'Fine gauge', 'Sleep', 'Jackets',
       'Swim', 'Trend', 'Jeans', 'Legwear', 'Shorts', 'Layering',
       'Casual bottoms', 'Chemises'])
plt.ylabel("Average Rating",size=15 ,weight = 'bold')
plt.title("Rating distribution of clothing products", size=18 ,weight = 'bold')
plt.show()
recommended = df[df['Recommended']==1]
not_recommended = df[df['Recommended']==0]
#ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)
plt.figure(figsize=(10,10))
ax3 = plt.xticks(rotation=45)
ax3 = sns.countplot(recommended[' Product name'], color="cyan", label = "Recommended")
ax3 = sns.countplot(not_recommended[' Product name'], color="blue",label = "Not Recommended")
ax3 = plt.title("Recommended Items in each Prodect name ")
ax3 = plt.legend()
plt.show()
