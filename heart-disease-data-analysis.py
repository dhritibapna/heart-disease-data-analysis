import pandas as pd

df = pd.read_csv('/Users/dhritibapna/Downloads/heartdisease.csv')  
print(df.shape)      
df.head()             
print(df.columns.tolist())
df['has_disease'] = df['num'].apply(lambda x: 1 if x > 0 else 0)
print(df.groupby('has_disease')['age'].mean())

import matplotlib.pyplot as plt

avg_age = df.groupby('has_disease')['age'].mean()
avg_age.plot(kind='bar', color=['steelblue', 'indianred'])
plt.xticks([0, 1], ['No Disease', 'Has Disease'])
plt.ylabel('Average Age')
plt.title('Average Age: Heart Disease vs No Disease')
plt.savefig('/Users/dhritibapna/Desktop/age_chart.png')
plt.show()

print(df.groupby('has_disease')['chol'].mean())
print(df['chol'].describe())
print((df['chol'] == 0).sum())
avg_chol = df.groupby('has_disease')['chol'].mean()
avg_chol.plot(kind='bar', color=['steelblue', 'indianred'])
plt.xticks([0, 1], ['No Disease', 'Has Disease'])
plt.ylabel('Average Cholesterol')
plt.title('Average Cholesterol: Heart Disease vs No Disease')
plt.savefig('/Users/dhritibapna/Desktop/chol_chart.png')
plt.show()
print(df[df['chol'] == 0]['has_disease'].value_counts())
