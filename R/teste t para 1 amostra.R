# teste T para uma amostra
# H0: mu = 65 (mu e a nossa famosa media mi e m0 e o numero que se quer medir)
# H1: mu <> 60

#gerar 36 amostras com media  65

amostras <- rnorm(36, mean = 65, sd=3.5)

# quero saber se a media da populacao e igual a 60 ou diferente
# H0: mu = 60
# H1: mu <> 65
t.test(amostras, mu=60)

hist(amostras)
