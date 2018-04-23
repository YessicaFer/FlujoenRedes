set terminal png truecolor
set output 'imgen150.eps'
set key off
set title '150 nodos'
set xlabel 'Probabilidad'
set ylabel 'Distancia promedio/cota (azul)'
set y2label 'Densidad promedio de cluster (rojo)'
set style line 1 lc rgb '#0000ff' lt 1 lw 1
set style line 2 lc rgb '#ff0000' lt 1 lw 1
plot[0:0.5][0:1] 'Resultadods150.csv' using 1:2 w lines ls 1, 'Resultadocluster150.csv' using 1:3 w lines ls 2
