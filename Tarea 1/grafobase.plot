set term png
set output 'grafobase1.png'
set xrange [0:1]
set yrange [0:1]
set pointsize 3
set size square
set key off
set arrow 1 from 0.936482, 0.293764 to 0.127108, 0.676182 nohead lw 3
set arrow 2 from 0.682831, 0.860378 to 0.936482, 0.293764 nohead lw 3
set arrow 3 from 0.535715, 0.990609 to 0.936482, 0.293764 nohead lw 3
set arrow 4 from 0.380697, 0.743977 to 0.380697, 0.743977 nohead lw 3
set arrow 5 from 0.380697, 0.743977 to 0.980209, 0.707202 nohead lw 3
set arrow 6 from 0.380697, 0.743977 to 0.083554, 0.547926 nohead lw 3
set arrow 7 from 0.122260, 0.906070 to 0.936482, 0.293764 nohead lw 3
set arrow 8 from 0.122260, 0.906070 to 0.682831, 0.860378 nohead lw 3
set arrow 9 from 0.122260, 0.906070 to 0.535715, 0.990609 nohead lw 3
set arrow 10 from 0.122260, 0.906070 to 0.083554, 0.547926 nohead lw 3
set arrow 11 from 0.122260, 0.906070 to 0.198071, 0.088181 nohead lw 3
set arrow 12 from 0.980209, 0.707202 to 0.535715, 0.990609 nohead lw 3
set arrow 13 from 0.083554, 0.547926 to 0.682831, 0.860378 nohead lw 3
set arrow 14 from 0.083554, 0.547926 to 0.980209, 0.707202 nohead lw 3
set arrow 15 from 0.083554, 0.547926 to 0.198071, 0.088181 nohead lw 3
set arrow 16 from 0.198071, 0.088181 to 0.535715, 0.990609 nohead lw 3
set arrow 17 from 0.198071, 0.088181 to 0.083554, 0.547926 nohead lw 3
show arrow
plot 'cir.dat' using 1:2 with points pt 7
quit()
