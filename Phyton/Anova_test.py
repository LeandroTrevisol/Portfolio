# %%

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#import dataframe

df = pd.read_excel("C:/Users/acer/Downloads/TE_Lista_2/TE_Lista_2/notas_precos.xlsx", usecols=["nota", "faixa_preco"])

#plotting

sns.boxplot(x="faixa_preco", y="nota", data=df)

#label

plt.xlabel("Faixa de Preco")
plt.ylabel("Nota")
plt.title("Boxplot de Relacionamento")

print(df.head())

# %%

from scipy.stats import f_oneway

# ANOVA calculus
# group according to "faixa de preco"

grupos = [group["nota"].values for name, group in df.groupby("faixa_preco")]

# ANOVA de uma amostra

f_stat, p_value = f_oneway(*grupos)

print("F=",f_stat)
print("P=",p_value)


# %%

# calculus of the mean of each group

mean_group = df.groupby("faixa_preco")["nota"].mean().reset_index()

print(mean_group)

