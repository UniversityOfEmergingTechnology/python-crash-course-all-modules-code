import pandas as pd

# Reading data from a CSV file
df = pd.read_json('ss.json')

# Filtering data
high_sales = df[df['Amount'] > 500]

# Summarizing data
summary = df.groupby('Product').sum()

print("Filtered Data:\n", high_sales)
print("Sales Summary:\n", summary)
