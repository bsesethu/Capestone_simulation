import pandas as pd

# Read the CSV file using a path
file_path = file_path = r"C:\Users\asus\Desktop\ZAIO\Capstone_simulation\Crime_data_A_newCSV.csv" 
df = pd.read_csv(file_path)


# Delete certain columns

columns_to_remove = ['Eastern Cape', 'Free State', 'Gauteng', 'KwaZulu-Natal', 'Limpopo', 'Mpumalanga', 'North West', 'Western Cape', 'July 2023 to \r\nSeptember 2023']
df = df.drop(columns=columns_to_remove)


# Dropping rows at positions 

df = df.drop(index=0)
df = df.iloc[:8]

# Drop all NaN columns
df = df.dropna(axis=1, how='all')

#Saving the new dataset into a new file
df.to_csv(r"C:\Users\asus\Desktop\ZAIO\Capstone_simulation\clean_dataset\nc_filtered_crime_data.csv", index=False)


print("CSV file processed and saved successfully.")
