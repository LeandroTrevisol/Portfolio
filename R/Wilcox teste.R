# Um grupo de 20 adolescentes fez a dieta dos pontos por um período de 1 mês.
# Verifique se houve redução de peso depois da dieta. Arquivo Dieta.xlsx. 
# Considere nível de significância de 5%.

library(readxl)
library(tidyverse)

Dieta <- read_excel("C:/Users/acer/Downloads/TE_Lista_2/TE_Lista_2/Dieta.xlsx")

Antes <- Dieta$Antes
Dep <- Dieta$Depois

shapiro.test(Antes)
shapiro.test(Dep)

pivotar <- Dieta %>%
  pivot_longer(cols = c(Antes, Depois),
               names_to = "Momento",
               values_to = "Peso")

# Gráfico de linhas por indivíduo
ggplot(pivotar, aes(x = Momento, y = Peso, fill = Momento)) +
  geom_boxplot() +
  labs(title = "Peso antes e depois da dieta",
       x = "Momento",
       y = "Peso (kg)") +
  theme_minimal()

wilcox.test(Antes, Dep, paired = TRUE)



