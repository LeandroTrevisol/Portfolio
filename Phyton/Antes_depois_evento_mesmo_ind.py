# %%

# Antes e depois de um tratamento
# Mesmos individuos
# amostra tamanho 30
# nivel de significancia 5%

import pandas as pd
from scipy.stats import shapiro


df = pd.read_excel("C:/Users/acer/Downloads/TE_Lista_2/TE_Lista_2/Colesterol.xlsx")
Antes = df["Antes_tratamento"]
Dep = df["Depois_tratamento"]


F_stats_Antes, P_Value_Antes = shapiro(Antes)
F_stats_Dep, P_Value_Dep = shapiro(Dep)

print(f"F_stats Antes = {F_stats_Antes:.3f}, P-Valor Antes = {P_Value_Antes:.4F}")
print(f"F_stats Dep = {F_stats_Dep:.3f}, P-Valor Depois = {P_Value_Dep:.4F}")





# %%

# Format the table to perform levene test
# use concat 

from scipy.stats import levene

# empilhar antes e depois

# pivotar = pd.DataFrame({
#     "Grupo": ["Antes"] * len(Antes) + ["Depois"] * len(Dep),
#     "Colesterol": pd.concat([Antes, Dep], ignore_index=True)
# })


stat, pvalue = levene(Antes, Dep, center="median")

print(f"F_Stat = {stat:.3f}")
print(f"P-Valor = {pvalue:.4f}")


# %%

# Test T for paired samples
# Test T - ttest_rel

from scipy.stats import ttest_rel


F_stat, P_Value = ttest_rel(Antes, Dep)

# check if calories decreased, sample Antes is "greater" than Dep

if F_stat > 0:
    p_value_one_sided = P_Value / 2
else:
    p_value_one_sided = P_Value / 2

print(f"F_stat = {F_stat:.3f}")
print(f"P_valor = {p_value_one_sided:.15f}")


# %%

import matplotlib.pyplot as plt
import seaborn as sns


# empilhar antes e depois

pivotar = pd.DataFrame({
     "Grupo": ["Antes"] * len(Antes) + ["Depois"] * len(Dep),
     "Colesterol": pd.concat([Antes, Dep], ignore_index=True)
 })

# plotting

plt.figure(figsize=(8,5))
sns.boxplot(x="Grupo", y="Colesterol", data=pivotar, palette="pastel")

# graph text

plt.title("Amostras Nr. Calorias antes e depois do tratamento")
plt.xlabel("Amostra Calorica")
plt.ylabel("Colesterol (mg/dL)")
plt.tight_layout()
