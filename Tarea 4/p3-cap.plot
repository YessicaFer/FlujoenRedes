set term eps
set output 'p3-cap.eps'
set xrange [-1:11]
set yrange [-1:11]
set pointsize 1
set size square
set key off
set arrow 1 from 8.000000, 5.000000 to 7.427051, 6.763356 nohead
set arrow 2 from 7.427051, 6.763356 to 8.000000, 5.000000 nohead
set arrow 3 from 7.427051, 6.763356 to 5.927051, 7.853170 nohead
set arrow 4 from 5.927051, 7.853170 to 7.427051, 6.763356 nohead
set arrow 5 from 5.927051, 7.853170 to 4.072949, 7.853170 nohead
set arrow 6 from 4.072949, 7.853170 to 5.927051, 7.853170 nohead
set arrow 7 from 4.072949, 7.853170 to 2.572949, 6.763356 nohead
set arrow 8 from 2.572949, 6.763356 to 4.072949, 7.853170 nohead
set arrow 9 from 2.572949, 6.763356 to 2.000000, 5.000000 nohead
set arrow 10 from 2.000000, 5.000000 to 2.572949, 6.763356 nohead
set arrow 11 from 2.000000, 5.000000 to 2.572949, 3.236644 nohead
set arrow 12 from 2.572949, 3.236644 to 2.000000, 5.000000 nohead
set arrow 13 from 2.572949, 3.236644 to 4.072949, 2.146830 nohead
set arrow 14 from 4.072949, 2.146830 to 2.572949, 3.236644 nohead
set arrow 15 from 4.072949, 2.146830 to 5.927051, 2.146830 nohead
set arrow 16 from 5.927051, 2.146830 to 4.072949, 2.146830 nohead
set arrow 17 from 5.927051, 2.146830 to 7.427051, 3.236644 nohead
set arrow 18 from 7.427051, 3.236644 to 5.927051, 2.146830 nohead
set arrow 19 from 7.427051, 3.236644 to 8.000000, 5.000000 nohead
set arrow 20 from 8.000000, 5.000000 to 7.427051, 3.236644 nohead
set arrow 21 from 4.072949, 7.853170 to 8.000000, 5.000000 nohead
set arrow 22 from 8.000000, 5.000000 to 4.072949, 7.853170 nohead
set arrow 23 from 4.072949, 2.146830 to 8.000000, 5.000000 nohead
set arrow 24 from 8.000000, 5.000000 to 4.072949, 2.146830 nohead
show arrow
plot 'p3-cap.dat' using 1:2 with points pt 7
quit()
