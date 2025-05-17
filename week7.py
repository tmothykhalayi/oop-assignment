# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
try:
    df = pd.read_csv(url)
    print("Dataset loaded successfully.")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Display the first few rows
print(df.head())

# Check the data types and missing values
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Fill missing values with the mean of each column (if any missing values exist)
df.fillna(df.mean(), inplace=True)

# Or drop rows with missing values
# df.dropna(inplace=True)

# Check if missing values are handled
print(df.isnull().sum())

# Task 2: Basic Data Analysis

# Compute basic statistics
print(df.describe())

# Group by 'species' and compute the mean of the numerical columns
grouped = df.groupby('species').mean()
print(grouped)

# Task 3: Data Visualization

# 3.1 Line Chart (Trends Over Time)
# Example: Plotting a line chart of average sepal length by index (simulating trends)
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x=df.index, y='sepal_length')
plt.title('Trend of Sepal Length Over Index')
plt.xlabel('Index')
plt.ylabel('Sepal Length')
plt.show()

# 3.2 Bar Chart (Comparison of a Numerical Value Across Categories)
# Bar chart comparing average petal length across species
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='species', y='petal_length')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length')
plt.show()

# 3.3 Histogram (Distribution of a Numerical Column)
# Histogram of sepal length
plt.figure(figsize=(10, 6))
sns.histplot(df['sepal_length'], kde=True, bins=20)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

# 3.4 Scatter Plot (Relationship Between Two Numerical Columns)
# Scatter plot for sepal length vs petal length
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='sepal_length', y='petal_length', hue='species')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.legend(title='Species')
plt.show()

# Error Handling (during Data Loading)
try:
    df = pd.read_csv(url)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("The dataset file was not found.")
except pd.errors.EmptyDataError:
    print("The dataset is empty.")
except Exception as e:
    print(f"An error occurred: {e}")
