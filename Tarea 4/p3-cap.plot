set term eps
set output 'p3-cap.eps'
set xrange [-.1:1.1]
set yrange [-.1:1.1]
set pointsize 1
set size square
set key off
set arrow 1 from 0.800000, 0.500000 to 0.742705, 0.676336 nohead
set arrow 2 from 0.742705, 0.676336 to 0.800000, 0.500000 nohead
set arrow 3 from 0.742705, 0.676336 to 0.592705, 0.785317 nohead
set arrow 4 from 0.592705, 0.785317 to 0.742705, 0.676336 nohead
set arrow 5 from 0.592705, 0.785317 to 0.407295, 0.785317 nohead
set arrow 6 from 0.407295, 0.785317 to 0.592705, 0.785317 nohead
set arrow 7 from 0.407295, 0.785317 to 0.257295, 0.676336 nohead
set arrow 8 from 0.257295, 0.676336 to 0.407295, 0.785317 nohead
set arrow 9 from 0.257295, 0.676336 to 0.200000, 0.500000 nohead
set arrow 10 from 0.200000, 0.500000 to 0.257295, 0.676336 nohead
set arrow 11 from 0.200000, 0.500000 to 0.257295, 0.323664 nohead
set arrow 12 from 0.257295, 0.323664 to 0.200000, 0.500000 nohead
set arrow 13 from 0.257295, 0.323664 to 0.407295, 0.214683 nohead
set arrow 14 from 0.407295, 0.214683 to 0.257295, 0.323664 nohead
set arrow 15 from 0.407295, 0.214683 to 0.592705, 0.214683 nohead
set arrow 16 from 0.592705, 0.214683 to 0.407295, 0.214683 nohead
set arrow 17 from 0.592705, 0.214683 to 0.742705, 0.323664 nohead
set arrow 18 from 0.742705, 0.323664 to 0.592705, 0.214683 nohead
set arrow 19 from 0.742705, 0.323664 to 0.800000, 0.500000 nohead
set arrow 20 from 0.800000, 0.500000 to 0.742705, 0.323664 nohead
show arrow
plot 'p3-cap.dat' using 1:2 with points pt 7
quit()
