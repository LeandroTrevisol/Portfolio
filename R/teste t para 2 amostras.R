# duas amostras
# duas medias
# teste t de duas amostras

library(readxl)
library(dplyr)
library(haven)
library(tidyverse)
library(ggplot2)
library(car) #teste F de levene

amostra <- read_excel("C:/Users/acer/Downloads/TE_Lista_2/TE_Lista_2/hospitais.xlsx")%>%

amostra %>%
  group_by(Hospital) %>%
  summarise(tempo_atend = mean(Tempo_Atendimento, na.rm = TRUE))

# pegando apenas hospital_1
g_1 <- amostra %>% 
  filter(Hospital=="Hospital_1")
shapiro.test(g_1$Tempo_Atendimento)

# pegando apenas hospital_2
g_1 <- amostra %>% 
  filter(Hospital=="Hospital_2")
shapiro.test(g_1$Tempo_Atendimento)


leveneTest(Tempo_Atendimento ~ Hospital, data=amostra)

t.test(Tempo_Atendimento ~ Hospital, data=amostra, var.equal=TRUE, conf.level = 0.99)
