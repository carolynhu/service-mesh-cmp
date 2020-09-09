install.packages("devtools")
devtools::install_github("twitter/BreakoutDetection")
library(BreakoutDetection)

p1 <- c(8457,8157,7682,9318,9277,8510)
p2 <- c(14662,15875,16376,16252,14777)
p3 <- c(15481,15883,14272,18042,19876)
p4 <- c(15131,18587,15117,15655,16421)
p5 <- c(15826,15766,15324,15349,15370)
p6 <- c(15605,15427,17201,15880,15577)
p7 <- c(15959,15288,15622,14066,16077)
p8 <- c(16773,17665,18139)
all = c(p1,p2,p3,p4, p5,p6,p7,p8)
plot(as.ts(all), col = "#27ccc0", lwd = 2)
res = breakout(all, min.size=3, method='multi', beta=.001, degree=1, plot=TRUE)
res$plot

