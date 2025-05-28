# %%

# Um grupo de 20 adolescentes fez a dieta dos pontos por um período de 1 mês. 
# Verifique se houve redução de peso depois da dieta. 
# Arquivo Dieta.xlsx. 
# Considere nível de significância de 5%.

import pandas as pd
from scipy.stats import shapiro


df = pd.read_excel("C:/Users/acer/Downloads/TE_Lista_2/TE_Lista_2/Dieta.xlsx")

Antes = df["Antes"]
Dep = df["Depois"]

F_statA, p_valA = shapiro(Antes)
F_StatD, p_valD = shapiro(Dep)

print(f"Shapiro F_stat Antes = {F_statA:.4f}")
print(f"Shapiro p_valor Antes = {p_valA:.4f}")

print(f"Shapiro F_stat Depois= {F_StatD:.4f}")
print(f"Shapiro p_valor Depois = {p_valD:.4f}")


# %%

from scipy.stats import wilcoxon


F_stat, P_Valor = wilcoxon(Antes, Dep)

print(f"Wilcox Paired Test f_stat = {F_stat:.4f}")
print(f"Wilcox Paired Test f_stat = {P_Valor:.4f}")

