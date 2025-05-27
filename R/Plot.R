library(tidyverse)
library(ggplot2)

x <- c(1:12)
Y <- c(40.0, 38.7, 35.2, 8.1, 24.3, 37.2, 39.4, 41.5, 42.3, 44.1, 46.7, 42.3)

plot(x,Y, xlab = "Months", ylab = "Temperature", main = "Monthly temperature 2024", type = "o", pch = 20, lwd = 2, col = "blue" )
