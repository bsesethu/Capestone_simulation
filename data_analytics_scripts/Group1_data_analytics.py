import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Loading the cleaned data from CSV
df_loaded = pd.read_csv("eastern_cape_gauteng_clean_data.csv")
print("\nLoaded from CSV:")
print(df_loaded)

#plotting of graph (data visualisation)

df_DataFrame = pd.melt(df_loaded, id_vars='CRIME CATEGORY',
                    value_vars=['Eastern Cape', 'Gauteng'],
                    var_name='Province', value_name='Crime Count')

print("\nSeaborn Barplot")
plt.figure(figsize=(12, 8))
sns.barplot(data=df_DataFrame, x='CRIME CATEGORY', y='Crime Count', hue='Province')
plt.xticks(rotation=50, ha='right')
plt.title("Crime Comparison: Eastern Cape vs Gauteng")
plt.show()


#Analysing the data 
#Descriptive Stats
print("\nDescriptive Stats:")
print(df_DataFrame.describe())

