import pandas as pd 

pd.options.display.max_columns = 999
pd.options.display.max_rows = 999


df = pd.read_csv("clean_dataset\eastern_cape_data.csv", sep=";")

df = df[["CRIME CATEGORY", "Eastern Cape", "Gauteng"]]

df = df.head(7)


print(df)
df.to_csv("clean_dataset/eastern_cape_gauteng_clean_data.csv", sep=",", index=False)