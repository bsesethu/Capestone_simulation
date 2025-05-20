import pandas as pd


file_path = "Crime_data_A_original.xlsx"
excel_file = pd.ExcelFile(file_path)

# Reload the sheet, skipping the first 4 rows to get proper headers
df = pd.read_excel(file_path, sheet_name="Sheet1", skiprows=4)

# Rename columns based on proper headers
df.columns = [
    "Crime Category", "Jul-Sep 2023", "Jul-Sep 2024", "Count Diff", "% Change",
    "Empty1", "Eastern Cape", "Free State", "Gauteng", "KwaZulu-Natal",
    "Limpopo", "Mpumalanga", "North West", "Northern Cape", "Western Cape"
]

# Drop unnecessary columns
df_clean = df[["Crime Category", "Western Cape", "Limpopo"]]

# Drop rows with missing or empty crime categories
df_clean = df_clean.dropna(subset=["Crime Category"])

# Show the cleaned data

#comparison of column 
comparison_column = df['Limpopo'] == df['Western Cape']
comparison_data = comparison_column == df['Jul-Sep 2024']

df['Comaprison Provincial'] = comparison_column.map({True: 'More', False: 'Less'})
df['Comparison National'] = comparison_data.map({True: 'More', False: 'Less'})

# df['National'] = df['Western Cape'] + df['Limpopo'] + df['Eastern Cape'] + df['Free State'] + df['Gauteng'] + df['KwaZulu-Natal'] + df['Mpumalanga'] + df['North West'] + df['Northern Cape'] #add thes columns and places in the column

# Show the cleaned data
print(df_clean.head())
print(df.head())
