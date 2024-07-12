# pyright: reportMissingModuleSource=false
import pandas as pd

df=pd.read_csv ("pass.csv")
print(df)

old = input("Cual es la Contraseña que quieres cambiar: ")
old = int(old)
new = "supass"

df.iloc [ old, 2 ] = new

df.to_csv('pass.csv', index=False)
print(df)