# %%

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt


# create a randam sample - normal distribution - with a mean of 65 calories

amostras = np.random.normal(loc=65, scale=3.5, size=36)

# loc = mean of the sample
# scale = standard deviation
# size = sample size


# test to check if the value atested match or differs from the mean of the samples
# 60 calories

t_stat, p_valor = stats.ttest_1samp(amostras, popmean=60)

print("Test t =", t_stat)
print("P_value =", p_valor)

# plot a hist graph

plt.figure(figsize=(8, 5))
plt.hist(amostras, bins=10, edgecolor="black", alpha=0.7)

# add mean line

plt.axvline(np.mean(amostras), color='red', linestyle='dashed', linewidth=2, label=f'Média: {np.mean(amostras):.2f}')

# add text

plt.title("Historama de 36 amostras aleatorias com distribuicao normal ")
plt.xlabel("Calorias")
plt.ylabel("Frequencia")
plt.legend()
plt.tight_layout()
