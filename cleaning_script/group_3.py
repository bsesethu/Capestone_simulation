import numpy as np
import pandas as pd

# Converting excel file to csv
# Read and store content of an excel file 
read_file = pd.read_excel("raw_dataset/Crime_data_A_original.xlsx") # Had to pip install openpylx
                                                                    # You direct from the current location to get to desired folder
# Write the dataframe object
# into csv file
read_file.to_csv ("Crime_data_A_newCSV.csv", index = None, header=True)
  
# read csv file and convert 
# into a dataframe object
df = pd.read_csv("Crime_data_A_newCSV.csv")
print(df.head(12))

# Condencing the dataframe to only include the 'contact crime' data
# by slice out
df_condensed = df.loc[0:8] # It includes 11
print('\n')
print(df_condensed)

df_condensed['Provincial percentages, North West'] = (df_condensed['North West'] / 10873.0) * 100 #NOTE Adding a new column and finding the provincial percentages
                                                                                                  # 10873.8 is the contact crime total for the North West
df_condensed['Provincial percentages, KZN'] = (df_condensed['KwaZulu-Natal'] / 28446.0) * 100 # 28446.0 contact crime total for KZN
print('\nContact crime by province, with added columns for provincial percentages for the two provinces')
print('\n')
print(df_condensed)

print('\nContact crime by province, with percentages of the provincial totals')
df_clean = df_condensed[['CRIME CATEGORY', 'North West', 'Provincial percentages, North West', 'KwaZulu-Natal', 'Provincial percentages, KZN']] #NOTE This is how to print only the columns we want
df_clean1 = df_clean.dropna() # Drop the missing data row
print(df_clean1) 

df_clean1.to_csv("clean_dataset/Provincial_KZN_NW_clean.csv", sep=",", index=False) # To save a csv of the dataframe to a certain folder