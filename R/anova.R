# uma amostra
# Testes estatisticos

library(readxl)
library(dplyr)
library(haven)
library(tidyverse)
library(ggplot2)
library(car) #teste F de levene

notas <- read_excel("C:/Users/acer/Downloads/TE_Lista_2/TE_Lista_2/notas_precos.xlsx")
notas <- notas[, c("nota","faixa_preco")]

notas %>%
  group_by(faixa_preco) %>%
  summarise(media_nota = mean(nota, na.rm = TRUE))

notas %>% 
  ggplot()+
  geom_boxplot(aes(x= faixa_preco, y=nota))

notas = aov(nota ~ faixa_preco, data=notas)
summary(notas)

notas %>%
  group_by(faixa_preco) %>%
  summarise(media_nota = mean(nota, na.rm = TRUE))



