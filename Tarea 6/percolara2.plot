set term eps
set output 'percolara2.eps'
set pointsize 1
set xrange[0:5]
set yrange[0:5]
set size square
unset xtics
unset ytics
set key off
set arrow 1 from 1.000000, 1.000000 to 1.000000, 2.000000 nohead
set arrow 2 from 1.000000, 2.000000 to 1.000000, 1.000000 nohead
set arrow 3 from 1.000000, 1.000000 to 2.000000, 1.000000 nohead
set arrow 4 from 2.000000, 1.000000 to 1.000000, 1.000000 nohead
set arrow 5 from 1.000000, 2.000000 to 1.000000, 3.000000 nohead
set arrow 6 from 1.000000, 3.000000 to 1.000000, 2.000000 nohead
set arrow 7 from 1.000000, 2.000000 to 2.000000, 2.000000 nohead
set arrow 8 from 2.000000, 2.000000 to 1.000000, 2.000000 nohead
set arrow 9 from 1.000000, 3.000000 to 1.000000, 4.000000 nohead
set arrow 10 from 1.000000, 4.000000 to 1.000000, 3.000000 nohead
set arrow 11 from 1.000000, 3.000000 to 2.000000, 3.000000 nohead
set arrow 12 from 2.000000, 3.000000 to 1.000000, 3.000000 nohead
set arrow 13 from 1.000000, 4.000000 to 2.000000, 4.000000 nohead
set arrow 14 from 2.000000, 4.000000 to 1.000000, 4.000000 nohead
set arrow 15 from 2.000000, 1.000000 to 2.000000, 2.000000 nohead
set arrow 16 from 2.000000, 2.000000 to 2.000000, 1.000000 nohead
set arrow 17 from 2.000000, 1.000000 to 3.000000, 1.000000 nohead
set arrow 18 from 3.000000, 1.000000 to 2.000000, 1.000000 nohead
set arrow 19 from 2.000000, 2.000000 to 2.000000, 3.000000 nohead
set arrow 20 from 2.000000, 3.000000 to 2.000000, 2.000000 nohead
set arrow 21 from 2.000000, 2.000000 to 3.000000, 2.000000 nohead
set arrow 22 from 3.000000, 2.000000 to 2.000000, 2.000000 nohead
set arrow 23 from 2.000000, 3.000000 to 2.000000, 4.000000 nohead
set arrow 24 from 2.000000, 4.000000 to 2.000000, 3.000000 nohead
set arrow 25 from 2.000000, 3.000000 to 3.000000, 3.000000 nohead
set arrow 26 from 3.000000, 3.000000 to 2.000000, 3.000000 nohead
set arrow 27 from 2.000000, 4.000000 to 3.000000, 4.000000 nohead
set arrow 28 from 3.000000, 4.000000 to 2.000000, 4.000000 nohead
set arrow 29 from 3.000000, 1.000000 to 3.000000, 2.000000 nohead
set arrow 30 from 3.000000, 2.000000 to 3.000000, 1.000000 nohead
set arrow 31 from 3.000000, 1.000000 to 4.000000, 1.000000 nohead
set arrow 32 from 4.000000, 1.000000 to 3.000000, 1.000000 nohead
set arrow 33 from 3.000000, 2.000000 to 3.000000, 3.000000 nohead
set arrow 34 from 3.000000, 3.000000 to 3.000000, 2.000000 nohead
set arrow 35 from 3.000000, 2.000000 to 4.000000, 2.000000 nohead
set arrow 36 from 4.000000, 2.000000 to 3.000000, 2.000000 nohead
set arrow 37 from 3.000000, 3.000000 to 3.000000, 4.000000 nohead
set arrow 38 from 3.000000, 4.000000 to 3.000000, 3.000000 nohead
set arrow 39 from 3.000000, 3.000000 to 4.000000, 3.000000 nohead
set arrow 40 from 4.000000, 3.000000 to 3.000000, 3.000000 nohead
set arrow 41 from 3.000000, 4.000000 to 4.000000, 4.000000 nohead
set arrow 42 from 4.000000, 4.000000 to 3.000000, 4.000000 nohead
set arrow 43 from 4.000000, 1.000000 to 4.000000, 2.000000 nohead
set arrow 44 from 4.000000, 2.000000 to 4.000000, 1.000000 nohead
set arrow 45 from 4.000000, 2.000000 to 4.000000, 3.000000 nohead
set arrow 46 from 4.000000, 3.000000 to 4.000000, 2.000000 nohead
set arrow 47 from 4.000000, 3.000000 to 4.000000, 4.000000 nohead
set arrow 48 from 4.000000, 4.000000 to 4.000000, 3.000000 nohead
show arrow
plot 'percolara2.dat' using 1:2 with points pt 7
quit()
