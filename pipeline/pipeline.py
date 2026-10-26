import sys 
import pandas as pd 

print("sys.argv:",sys.argv)
month = int(sys.argv[1])
df = pd.DataFrame({"day": [1, 2], "passengers": [3, 4]})
df['month'] = month
print(df.head())

df.to_parquet(f"data_{month}.parquet")

print(f"hello pipeline,month:{month}")
