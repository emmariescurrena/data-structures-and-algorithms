import pandas as pd

df=pd.read_csv ("pass.csv")

print(df)
rows = input("Que fila quieres borrar: ")
rows=int(rows)

df.drop(df.index[[rows]], axis=0, inplace=True)

df.to_csv('pass.csv', index=False)
print(df)
