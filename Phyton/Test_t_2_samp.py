# %%

# 2 mediasTeste T com duas amostras
# testar normalidade na distribuicao
# testar homogenidade na variancia

import pandas as pd
import seaborn as sns
from scipy.stats import f_oneway
import matplotlib.pyplot as plt

# import dataframe

df = pd.read_excel("C:/Users/acer/Downloads/TE_Lista_2/TE_Lista_2/Hospitais.xlsx", usecols="a:b")


# checking the mean of each group separately. 

meangroups = df.groupby("Hospital")["Tempo_Atendimento"].mean().reset_index()
print(meangroups)

#plotting

sns.boxplot(x="Hospital", y="Tempo_Atendimento", data=df)

#veryfied by visualisation that both samples differs. 


# %%

from scipy.stats import shapiro

# Separate each group 
# implement shapiro test - sample between 3 and 4000
# checking if the distribution is normal

group1 = df[df["Hospital"] == "Hospital_1"]["Tempo_Atendimento"]
group2 = df[df["Hospital"] == "Hospital_2"]["Tempo_Atendimento"]


# Shapiro test

f_stat, p_value = shapiro(group1)
f_statb, p_valueb = shapiro(group2)


print(f"F_stat = {f_stat:.3f}, p-value = {p_value:.4f}")
print(f"F_statb = {f_statb:.3f}, p_valueb = {p_valueb:.4f}")


# %%

# teste Levene

from scipy.stats import levene


f_stat, p_value = levene(group1, group2, center="median")

print(f"F_stat = {f_stat:.3f}")
print(f"P-Value = {p_value:.4f}")
# %%

# Test T for two samples after checking the distribution and the variance. 

from scipy.stats import ttest_ind


f_stat, p_value = ttest_ind(group1, group2, equal_var=True)


print(f"F_stat = {f_stat:.3f}")
print(f"P-Value = {p_value:.10f}")


