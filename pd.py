import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('Bank Customer Churn Prediction.csv')
print(df)
plt.scatter(df['tenure'], df['balance'], color='blue',  alpha=0.5)
plt.title('tenure vs.balance')
plt.xlabel('tenure')
plt.ylabel('balance')
plt.show()
estimated_salary = df['estimated_salary']
plt.figure(figsize=(8, 6))  
plt.hist(estimated_salary, bins=20, color='skyblue', edgecolor='black') 
plt.title('Distribution of Estimated Salary')
plt.xlabel('Frequency')
plt.ylabel('estimated_salary')
plt.show() 
country_counts = df['country'].value_counts()

plt.figure(figsize=(8, 6))  
plt.pie(country_counts, labels=country_counts.index, autopct='%1.1f%%', colors=['red', 'gold','orange'])  
plt.axis('equal') 
plt.show()

