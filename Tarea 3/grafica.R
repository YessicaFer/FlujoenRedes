pdf("FloydWarshallFordFulkerson.pdf")
plot(seq(1:11)^3, type="l" , xlab="Eje x", ylab="Eje y", col="blue", lwd=2)
legend("topleft",col=c("Blue"), legend =c("Función Cubica"), lwd=3, bty = "n")
graphics.off()