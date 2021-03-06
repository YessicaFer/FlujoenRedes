library(readr)
library(prob)
Dirigido <- read.csv("tDirigidoTT.csv", header=FALSE)
NDirigido <- read.csv("tNoDirigidoTF.csv", header=FALSE)

#El n�mero 11 en los datos corresponde a la cantidad de tama�os diferentes de grafos y el 6 a las repeticiones de cada tama�o

TDirigido <- data.frame()
for (i in 1:11){
  TDirigido <- rbind(TDirigido, Dirigido[((6*i)-5):(6*i),])
}
shapiro.test(TDirigido[,1]) #No es normal
pdf("TDirigidoTT.pdf")
boxplot(t(TDirigido), main="Tiempo vs N", xlab=c("N�mero de nodos"), ylab=c("Tiempo (segundos)"), plot=TRUE)
par(new=TRUE, pty="m", xaxt="n", yaxt="n")
plot(seq(1:11)^3, type="l" , xlab="", ylab="", col="blue", lwd=2)
legend("topleft",col=c("Blue"), legend =c("Funci�n C�bica"), lwd=3, bty = "n")

TNoDirigido <- data.frame()
for (i in 1:11){
  TNoDirigido <- rbind(TNoDirigido, NDirigido[((6*i)-5):(6*i),])
}
shapiro.test(TNoDirigido[,1]) #No es normal
pdf("TNoDirigidoTF.pdf")
boxplot(t(TNoDirigido), main="Tiempo vs N", xlab=c("N�mero de nodos"), ylab=c("Tiempo (segundos)"), plot=TRUE)
par(new=TRUE, pty="m", xaxt="n", yaxt="n")
plot(seq(1:11)^3, type="l" , xlab="", ylab="", col="red", lwd=2)
legend("topleft",col=c("red"), legend =c("Funci�n C�bica"), lwd=3, bty = "n")
graphics.off()