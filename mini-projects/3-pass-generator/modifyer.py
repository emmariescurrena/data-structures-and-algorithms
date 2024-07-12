# pyright: reportMissingModuleSource=false
import pandas as pd

df=pd.read_csv ("pass.csv")
print(df)

old = input("Cual es el Username que quieres cambiar: ")
old = int(old)
new = input("Introduce el nuevo Username: ")

df.iloc [ old, 1 ] = new

df.to_csv('pass.csv', index=False)
print(df)
