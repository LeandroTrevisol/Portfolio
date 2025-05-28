# Teste 2 x 3
# Amostra 60 leitores
# 3 livros como opcao
# cada leitor escolhe um livro que gostou

# Teste qui-quadrado
# frequencia de escolha

library(tidyverse)
library(tidyr)

coletado <- c(29,15,16)

#H0 - teste esperado

esperado <- rep(60/3,3)


resultado <- chisq.test(x = coletado, p = c(1/3,1/3,1/3))

print(resultado)



  


  

