import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('news_test.csv')

# Get the keys (column headers)
keys = df.columns.tolist()

# Print the keys
print(keys)