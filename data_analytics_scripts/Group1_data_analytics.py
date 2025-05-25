import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the data from the CSV file.
df = pd.read_csv("eastern_cape_gauteng_clean_data.csv")
print(df)
df = df[["CRIME CATEGORY", "Eastern Cape", "Gauteng"]]
df = df.head(7)

# Plotting
plt.figure(figsize=(10, 6))
bar_width = 0.35
x = range(len(df))

plt.bar(x, df["Eastern Cape"], width=bar_width, label="Eastern Cape", color='black')
plt.bar([i + bar_width for i in x], df["Gauteng"], width=bar_width, label="Gauteng", color='grey')

# Add labels and title
print("\nSeaborn Barplot")
plt.xlabel("Crime Category")
plt.ylabel("Number of Cases")
plt.title("Crime Statistics: Eastern Cape vs Gauteng")
plt.xticks([i + bar_width / 2 for i in x], df["CRIME CATEGORY"], rotation=45, ha="right")
plt.legend()
plt.tight_layout()
plt.show()


#Analysing the data 
#Descriptive Stats
# print("\nDescriptive Stats:")
# print(df_DataFrame.describe())