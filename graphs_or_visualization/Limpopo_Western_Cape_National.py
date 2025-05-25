import numpy as np
import pandas as pd


file_path = "cleaning_script/Limpopo/Crime_data_A_original.xlsx"
excel_file = pd.ExcelFile(file_path)

#Reload the sheet, skipping the first 4 rows to get proper headers,
df = pd.read_excel(file_path, sheet_name="Sheet1", skiprows=4)

import matplotlib.pyplot as plt

import numpy as np

#Sorting the necessary data manually

x = np.arange(8)
Limpopo = [243,1091,269,3054,2487,727,1831,9702]
Western_Cape=[1063,1546,1104,5350,10051,2583,6227,27924]
National= [6545,12765, 7061,42721,44722,11692,35429,160935]

#Bar Graph showing Limpopo and Western Cape vs the National stats
width = 0.3

# plot data in grouped manner of bar type
plt.bar(x-0.3, Limpopo, width, color='cyan')
plt.bar(x-0.6, Western_Cape, width, color='green')
plt.bar(x, National, width, color='orange')
plt.xticks(x, ['Murder', 'Sexual offences', 'Attempted murder', 'Assault with the intent to inflict grievous bodily harm', 'Common assault', 'Common robbery', 'Robbery with aggravating circumstances', 'Contact Crimes'])
plt.xticks(x,rotation=15, ha='right')
plt.xlabel("Types of Crimes")
plt.ylabel("Number of Cases")
plt.legend(["Limpopo","Western Cape", "National"])
plt.show()