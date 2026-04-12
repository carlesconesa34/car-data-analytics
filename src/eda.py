import pandas as pd

df = pd.read_csv("data/raw/car_price_dataset.csv")

# Load data
data_shape = df.shape
print(data_shape)
print()

# Overview
data_preview = df.head(10)
print(data_preview)
print()

# Null values
null_values = df.isnull().sum()
print(f"Null values:\n\n {null_values}\n")

# Duplicated values
duplicated_values = df.duplicated().sum()
print(f"Duplicated values: {duplicated_values}\n")

# Statistics
data_description = df.describe()
print(data_description)
print()

# Categorical columns
brand_count = df["Brand"].value_counts()
print(brand_count)
print()

fuel_type_count = df["Fuel_Type"].value_counts()
print(fuel_type_count)
print()

transmission_count = df["Transmission"].value_counts()
print(transmission_count)
print()

doors_count = df["Doors"].value_counts()
print(doors_count)
print()
