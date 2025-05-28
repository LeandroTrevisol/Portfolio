# %%

import pandas as pd
from scipy.stats import friedmanchisquare


df = pd.read_excel("C:/Users/acer/Downloads/TE_Lista_2/TE_Lista_2/Banco.xlsx")

BancoA = df["A"]
BancoB = df["B"]
BancoC = df["C"]


F_stat, P_Valor = friedmanchisquare(BancoA, BancoB, BancoC)

print(f"F_Stat do Teste Friedman = {F_stat:.4f}")
print(f"P_valor do Teste Friedman = {P_Valor:.4f}")
