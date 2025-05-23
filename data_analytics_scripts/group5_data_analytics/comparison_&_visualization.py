import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r"C:\Users\asus\Desktop\ZAIO\Capstone_simulation\clean_dataset\nc_filtered_crime_data_group5.csv"
df = pd.read_csv(file_path)
# print(df.head())



df.plot(kind='bar')

plt.title("Crime Comparison Provincial vs National 2024")
plt.xlabel("Crime Category")
plt.ylabel("Values")
plt.xticks(rotation=0)
plt.legend(title="Year")
plt.tight_layout()

plt.show()


