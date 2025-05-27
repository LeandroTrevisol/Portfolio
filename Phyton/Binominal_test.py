# %%

import pandas as pd
from scipy.stats import binomtest

# 6)	Um grupo de 20 consumidores fez um teste de degustação com dois tipos de cerveja (Marca A e Marca B). Ao final, escolheram uma das marcas, como vemos a seguir. Teste a hipótese de não há diferença na preferência dos consumidores, ao nível de significância de 5%.
# Eventos	Marca A	Marca B	Total
# Frequência	8	12	20

resultado = binomtest(k=8, n=20, p=0.5, alternative="two-sided")

print(f"Resultado do teste Binominal = {resultado.pvalue:.4f}" )


