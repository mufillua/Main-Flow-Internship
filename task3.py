import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("C:\CODING\MainFlow Internship\householdtask3.csv")

# Create a bar chart for income and years
plt.figure(figsize=(10, 6))
plt.bar(data['year'], data['income'], color='skyblue')
plt.xlabel('Year')
plt.ylabel('Income')
plt.title('Income based on Years')
plt.xticks(rotation=45)
plt.show()

# Create a line chart for expenditure and income trends
plt.figure(figsize=(10, 6))
plt.plot(data['year'], data['expenditure'], marker='o', label='expenditure', color='blue')
plt.plot(data['year'], data['income'], marker='s', label='income', color='green')
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Expenditure and Income Trends')
plt.xticks(rotation=45)
plt.legend()
plt.show()
