import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('C:\CODING\MainFlow Internship\Salary_Data.csv')

# Handle missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

print("DataFrame after handling missing values:")
print(df)

# Visualize the distribution of variables
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.histplot(df['Age'], kde=True, color='blue')
plt.title('Age Distribution')

plt.subplot(1, 2, 2)
sns.histplot(df['Salary'], kde=True, color='green')
plt.title('Salary Distribution')

plt.show()

# Box plots for Age and Salary
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.boxplot(y=df['Age'], color='blue')
plt.title('Age Box Plot')

plt.subplot(1, 2, 2)
sns.boxplot(y=df['Salary'], color='green')
plt.title('Salary Box Plot')

plt.show()

# Scatter plot to identify outliers
plt.figure(figsize=(8, 6))
plt.scatter(df['Age'], df['Salary'], color='purple')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Scatter Plot of Age vs. Salary')
plt.show()

# Correlation matrix and heatmap
corr_matrix = df[['Age', 'Salary']].corr()
print("Correlation Matrix:")
print(corr_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()
