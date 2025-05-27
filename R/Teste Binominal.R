library(tidyverse)

# 6)	Um grupo de 20 consumidores fez um teste de degustação com dois tipos de cerveja (Marca A e Marca B). 
# Ao final, escolheram uma das marcas, como vemos a seguir. 
# Teste a hipótese de não há diferença na preferência dos consumidores, 
# ao nível de significância de 5%.
# Eventos	Marca A	Marca B	Total
# Frequência	8	12	20

binom.test(12, 20, p=0.5)

