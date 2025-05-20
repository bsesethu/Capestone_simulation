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


# df_new = df_condensed.dropna() # Drop missing data. drops all rows
# Remove other provinces, leave only KZN and North West


df_condensed['Provincial percentages, North West'] = (df_condensed['North West'] / 10873.0) * 100 #NOTE Adding a new column and finding the provincial percentages
                                                                                                  # 10873.8 is the contact crime total for the North West
print('\nContact crime by province, with an added column provincial percentages for the North West province')
print('\n')
print(df_condensed)

