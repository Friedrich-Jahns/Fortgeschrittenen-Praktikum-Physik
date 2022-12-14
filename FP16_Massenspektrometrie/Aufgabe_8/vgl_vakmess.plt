set term png 
set output 'druck_vgl.png'
set grid
set ylabel 'Totaldruck COMBI VAC [Torr]' rotate by 90
set xlabel 'Totaldruck HAL 7 RC RGA 100 [Torr]'
set format y '%.1tx10^{%T}'

A = 28.9
B = 5.1
f(x) = A*x+B
fit f(x) "Data/data_gnu.dat" using 1:3:2:4 xyerrors via A, B

plot 'Data/data_gnu.dat' using 1:3:2:4 lc "red" ps 1 pt 7 title "Data" with xyerrorbars,\
f(x) t 'Fit' lw 1.55 lc 'black'