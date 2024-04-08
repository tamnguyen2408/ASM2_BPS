import pandas as pd

# Read data from a CSV file with a semicolon (;) delimiter character.
df = pd.read_csv('data.csv', sep=';')


# Remove data rows that have at least one null field
df = df.dropna()

# Displays data after removing rows with all blank fields
print("data after removing rows with all empty fields:")
print(df)
print()

# Remove duplicate lines
duplicate_rows = df[df.duplicated()]
if not duplicate_rows.empty:
    print("there is noisy data - lines are duplicated. Remove duplicate lines")
    df = df.drop_duplicates()
else:
    print("no noisy data - no duplicated lines")

# Displays data after removal
print("Data after removing duplicate lines and having NaN value:")
print(df)

# Handling Missing Data
missing_data = df.isnull().sum()
print("Missing data in each column: ")
print(missing_data)


# Handling column "Date"
# Convert the "Date" column to a valid date format, ignoring invalid values
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Display data after processing the "Date" column
print("Data after processing column 'Date':")
print(df)
print()

# Handle the column "Quantity"
# Convert the "Quantity" column to an integer data type, ignoring invalid values
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')

# Display data after processing the "Quantity" column
print("Data after processing column 'Quantity':")
print(df)
print()

# Store the cleaned data into a new CSV file
df.to_csv('cleaned_data.csv', index=False)

print("The data was cleaned and saved to file'cleaned_data.csv'.")
