# %%

# Um grupo de 60 leitores fez uma avaliação de três livros de romance e, 
# ao final, escolheram uma das três opções. 
# Teste a hipótese nula de que não há preferência dos leitores, 
# com nível de significância de 5%.

# teste 2x3
# 60 leitores
# 3 livros
# h0 = 20
# H = mu = 20
# H = MU <> 20

import numpy as np
from scipy.stats import chisquare


coletado = np.array([29,15,16])
esperado = np.array([60/3] * 3)

# Chisquare test - 2x3

F_stat, P_value = chisquare(f_obs = coletado, f_exp = esperado)

print(f"F-Stat = {F_stat:.4f}")
print(f"P_Valor = {P_value:.4f}")






