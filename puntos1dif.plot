set term png
set output 'nod1.png'
set xrange [0:1]
set yrange [0:1]
set pointsize 3
set size square
set key off
plot 'puntosdif.dat' using 1:2:3 with points pt var
quit()
