import pandas as pd
from raw_dataset import Crime_data_A_original


file_path = ("raw_dataset/Crime_data_A_original.xlsx")
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

#Show the cleaned data,
print(df_clean.head())

#Comparing Limpopo to National stats
#df['Comparison'] = comparison_result.map({True: 'Match', False: 'Mismatch'})


