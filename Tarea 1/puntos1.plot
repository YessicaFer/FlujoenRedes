set term png
set output 'nod.png'
set xrange [0:1]
set yrange [0:1]
set pointsize 3
set size square
set key off
plot 'nodos.dat' using 1:2 with points pt 7
quit()
