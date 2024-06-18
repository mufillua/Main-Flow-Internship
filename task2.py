import pandas as pd

# Step 1: Load the CSV file into a Pandas DataFrame
df = pd.read_csv('C:\CODING\MainFlow Internship\dataset_task2.csv')
print("Original DataFrame:")
print(df)

# Step 2: Filtering Data Based on Conditions
# Filter data where ChipRate > 15
filtered_df = df[df['ChipRate'] > 15]
print("\nFiltered DataFrame (ChipRate > 15):")
print(filtered_df)

# Step 3: Handling Missing Values
# Fill missing values in ChipRate with the mean ChipRate
df['ChipRate'].fillna(df['ChipRate'].mean(), inplace=True)

# Fill missing values in UCZAA with the mean UCZAA
df['UCZAA'].fillna(df['UCZAA'].mean(), inplace=True)

print("\nDataFrame after handling missing values:")
print(df)

# Step 4: Calculating Summary Statistics
# Calculate summary statistics
summary_stats = df.describe()
print("\nSummary Statistics:")
print(summary_stats)
