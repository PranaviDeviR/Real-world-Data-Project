import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

output_folder = 'plots'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
df = pd.read_csv('healthcare_dataset.csv')
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])
df['Length_of_Stay'] = (df['Discharge Date'] - df['Date of Admission']).dt.days

print(df.info())
print(df.describe())

plt.figure(figsize=(12, 6))
sns.boxplot(x='Medical Condition', y='Billing Amount', data=df)
plt.title('Distribution of Billing Amount by Medical Condition')
plt.xticks(rotation=45)
plt.savefig(os.path.join(output_folder, 'billing_by_condition.png'))
plt.close()

plt.figure(figsize=(12, 6))
avg_stay = df.groupby('Medical Condition')['Length_of_Stay'].mean().sort_values()
avg_stay.plot(kind='bar', color='skyblue')
plt.title('Average Length of Stay by Medical Condition')
plt.ylabel('Days')
plt.savefig(os.path.join(output_folder, 'stay_by_condition.png'))
plt.close()

plt.figure(figsize=(10, 5))
sns.barplot(x='Insurance Provider', y='Billing Amount', data=df)
plt.title('Average Billing Amount by Insurance Provider')
plt.savefig(os.path.join(output_folder, 'billing_by_insurance.png'))
plt.close()

numerical_cols = ['Age', 'Billing Amount', 'Length_of_Stay']
plt.figure(figsize=(8, 6))
sns.heatmap(df[numerical_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.savefig(os.path.join(output_folder, 'correlation_heatmap.png'))
plt.close()

print(f"Analysis complete. Plots saved in the '{output_folder}' folder.")
