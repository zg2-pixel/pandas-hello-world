import pandas as pd

# =====================================
# 1. LOAD DATA
# =====================================
df = pd.read_excel('sensor_data.xlsx')
print("Data Loaded!\n")


# =====================================
# 2. EXPLORE DATA
# =====================================
print("First few rows:")
print(df.head())

print("\n\nBasic Info:")
print(df.info())

print("\n\nStatistics:")
print(df.describe())


# =====================================
# 3. CLEAN DATA
# =====================================
print("\n\nMissing values:")
print(df.isnull().sum())

# Fill missing temperature with average
df['Temperature'].fillna(df['Temperature'].mean(), inplace=True)
print("\nMissing values fixed")


# =====================================
# 4. ANALYZE DATA
# =====================================

# Average temperature by equipment
print("\n\nAverage Temperature by Equipment:")
print(df.groupby('Equipment')['Temperature'].mean())

# Count equipment status
print("\n\nStatus Counts:")
print(df['Status'].value_counts())

# Find high temperature readings
print("\n\nHigh Temperature (>50°C):")
hot_equipment = df[df['Temperature'] > 50]
print(hot_equipment[['Date', 'Equipment', 'Temperature', 'Status']])


# =====================================
# 5. ADD NEW COLUMN
# =====================================
# Flag equipment needing maintenance
df['Needs_Check'] = df['Temperature'] > 50
print("\n\nEquipment to Service:")
print(df[df['Needs_Check']][['Equipment', 'Temperature', 'Status']])


# =====================================
# 6. EXPORT RESULTS
# =====================================
df.to_excel('sensor_data_analyzed.xlsx', index=False)
print("\nResults saved to sensor_data_analyzed.xlsx")