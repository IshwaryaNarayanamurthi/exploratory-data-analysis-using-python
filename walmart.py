import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df=pd.read_csv("Walmart_Store_sales.csv")
print(df)

plt.plot(df['Date'], df['Weekly_Sales'], marker='o', linestyle='-')
plt.title('Weekly Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Weekly Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 6))
df.groupby('Holiday_Flag')['Weekly_Sales'].mean().plot(kind='bar', color=['blue', 'red'])
plt.title('Impact of Holidays on Sales')
plt.xlabel('Holiday Flag')
plt.ylabel('Average Weekly Sales')
plt.xticks([0, 1], ['Non-Holiday', 'Holiday'], rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 6))
plt.scatter(df['Temperature'], df['Weekly_Sales'], alpha=0.5)
plt.title('Temperature vs. Weekly Sales')
plt.xlabel('Temperature')
plt.ylabel('Weekly Sales')
plt.grid(True)
plt.tight_layout()
plt.show()
holiday_temperatures = df[df['Holiday_Flag'] == 1]['Temperature']
non_holiday_temperatures = df[df['Holiday_Flag'] == 0]['Temperature']
plt.figure(figsize=(10, 6))
plt.hist(holiday_temperatures, bins=20, alpha=0.5, label='Holiday', color='blue')
plt.hist(non_holiday_temperatures, bins=20, alpha=0.5, label='Non-Holiday', color='green')
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.title('Distribution of Temperatures During Holidays vs. Non-Holidays')
plt.legend()
plt.show()
selected_columns = ['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']
df_selected = df[selected_columns]
correlation_matrix = df_selected.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()
holiday_sales = df[df['Holiday_Flag'] == 1]['Weekly_Sales']
non_holiday_sales = df[df['Holiday_Flag'] == 0]['Weekly_Sales']
plt.figure(figsize=(10, 6))
sns.boxplot(x='Holiday_Flag', y='Weekly_Sales', data=df)
plt.title('Distribution of Weekly Sales During Holidays vs. Non-Holidays')
plt.xlabel('Holiday')
plt.ylabel('Weekly Sales')
plt.xticks([0, 1], ['Non-Holiday', 'Holiday'])
plt.show()


