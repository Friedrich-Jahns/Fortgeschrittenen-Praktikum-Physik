set term png 
set output 'druck_vgl.png'
set grid
# set yrange [0.02:40]
# set xrange [-40:40]
set ylabel 'Totaldruck COMBI VAC'
set xlabel 'Totaldruck HAL 7 RC RGA 100'


A = 28.9
B = 5.1
f(x) = A*x+B
fit f(x) "Data/data_gnu.dat" using 1:3:2:4 xyerrors via A, B

plot 'Data/data_gnu.dat' using 1:3:2:4 title "center" with xyerrorbars,\
f(x) t 'Fit'