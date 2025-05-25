import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df_NW_KZN = pd.read_csv('clean_dataset/Provincial_KZN_NW_clean.csv')
print(df_NW_KZN)

# Need to remove the last row, the totals row. For a cleaner graph
df_NW_KZN.drop(index= 7, inplace= True) #NOTE How to remove a specific row from the df

# Plotting
y = df_NW_KZN['Provincial percentages, North West'] #NOTE Double square bracket for a single column. NOTE A single square bracket does the same thing, just without the column heading
mylabels = df_NW_KZN['CRIME CATEGORY'] # NOTE Single square brackets are the way to go here

fig, ax = plt.subplots()
ax.set_title('Provincial percentages for Contact Crime, North West')
ax.pie(y, labels= mylabels, autopct='%1.1f%%')
plt.show()

    # For KZN
y_KZN = df_NW_KZN['Provincial percentages, KZN'] 
mylabels_KZN = df_NW_KZN['CRIME CATEGORY'] 

fig1, ax1 = plt.subplots()
ax1.set_title('Provincial percentages for Contact Crime, KZN')
ax1.pie(y_KZN, labels= mylabels_KZN, autopct='%1.1f%%')
plt.show()

# Plotting National. We can't really plot national, we need all the other provinces' national data
print('\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
df_National = pd.read_csv('clean_dataset/National_KZN_NW_clean.csv')
print(df_National)

# Compare the two provinces to each other
bar_width = 0.35
x = np.arange(len(df_NW_KZN['CRIME CATEGORY']))

# Creating the bar chart
plt.bar(x, df_NW_KZN['Provincial percentages, North West'], width= bar_width, label= 'North West')
plt.bar(x + bar_width / 2, df_NW_KZN['Provincial percentages, KZN'], width= bar_width, label= 'KZN')

plt.xlabel('Province')
plt.ylabel('Percentage of provincial total')
plt.title('Contact crime as percentage of provincial total')
plt.xticks(x + bar_width / 2, df_NW_KZN['CRIME CATEGORY'], rotation= 9) # Center x ticks. 'rotation' so that words don't overlap
plt.legend()
plt.show()
