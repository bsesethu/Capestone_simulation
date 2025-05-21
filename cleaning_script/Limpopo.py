import pandas as pd


file_path = ("cleaning_script/Limpopo/Crime_data_A_original.xlsx")
excel_file = pd.ExcelFile(file_path)

#Reload the sheet, skipping the first 4 rows to get proper headers,
df = pd.read_excel(file_path, sheet_name="Sheet1", skiprows=4)

#Rename columns based on proper headers,
df.columns = [
    "Crime Category", "Jul-Sep 2023", "Jul-Sep 2024", "Count Diff", "% Change",
    "Empty1", "Eastern Cape", "Free State", "Gauteng", "KwaZulu-Natal",
    "Limpopo", "Mpumalanga", "North West", "Northern Cape", "Western Cape"
]

#Drop unnecessary columns,
df_clean = df[["Crime Category","Jul-Sep 2023", "Jul-Sep 2024", "Limpopo"]]

#Drop rows with missing or empty crime categories,
df_clean = df_clean.dropna(subset=["Crime Category"])


#Comparing Limpopo to National stats
#df['Comparison'] = comparison_result.map({True: 'Match', False: 'Mismatch'})
comparison_column = df['Limpopo'] == df['Western Cape']
comparison_data = comparison_column == df['Jul-Sep 2024']

df['Comparison'] = comparison_data.map({True: 'More', False: 'Less'})


#Show the cleaned data,
print(df.head())