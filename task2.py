import pandas as pd

# Load the CSV file
file_path = 'C:/Users/umesh/Downloads/states_by_country.csv'
df = pd.read_csv(file_path)

print(type(df))
print("\n")
print(df.info)
print("\n")

print("Descibing Dataframe")
print(df.describe())

# Display the first few rows of the dataframe
print("\nFirst few rows of the Dataframe:\n")
print(df.head())

# Handling Missing Values
df_filled = df.fillna('Unknown')
df_dropped = df.dropna()
print("\nDataFrame with missing values filled:\n")
print(df_filled.head())
print("\nDataFrame with missing values dropped:\n")
print(df_dropped.head())

# Removing Duplicates
print("\nDataFrame without duplicates:\n")
print(df.drop_duplicates())

# Filtering Data
filtered_df = df[df['Country Code'] == 'AL']
print("\nFiltered DataFrame where Country Code is 'AL':\n")
print(filtered_df.head())

# Sorting Data
sorted_df = df.sort_values(by='State Name')
print("\nDataFrame sorted by State Name:\n")
print(sorted_df.head())

# Grouping Data
grouped_df = df.groupby('Country Name').count()
print("\nGrouped DataFrame by Country Name with state counts:\n")
print(grouped_df['State Name'].head())
