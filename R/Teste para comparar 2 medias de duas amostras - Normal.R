# Testes estatisticos

library(readxl)
library(haven)
library(tidyverse)
library(car) #teste F de levene


g_a <- normtemp %>% 
  filter(Gender=="Male")
shapiro.test(g_a$BodyTemp)

hist(g_a$BodyTemp)

g_b <- normtemp %>% 
  filter(Gender=="Female")
shapiro.test(g_b$BodyTemp)

hist(g_b$BodyTemp)


leveneTest(BodyTemp ~ Gender, data = normtemp)

t.test(BodyTemp ~ Gender, data = normtemp,alternative="two.sided", var.equal = TRUE)
