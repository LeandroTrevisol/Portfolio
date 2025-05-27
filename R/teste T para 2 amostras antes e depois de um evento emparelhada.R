# teste de 2 amostra
# antes e depois do tratamento
# tamanho 30

library(readxl)
library(dplyr)
library(haven)
library(tidyverse)
library(tidyr)
library(car)

amostra <- read_excel("C:/Users/acer/Downloads/TE_Lista_2/TE_Lista_2/Colesterol.xlsx")

antes <- amostra$Antes_tratamento
dep <- amostra$Depois_tratamento

shapiro.test(antes$Antes_tratamento)

shapiro.test(dep$Depois_tratamento)

pivotar <- amostra %>%
  pivot_longer(cols = c(Antes_tratamento,Depois_tratamento), 
               names_to = "Grupo",
               values_to ="Colesterol")

leveneTest(Colesterol ~ Grupo, data=pivotar)

t.test(antes, dep, paired = TRUE, alternative = "greater")

pivotar %>% 
  ggplot() + 
  geom_boxplot(aes(x=Grupo, y=Colesterol))



