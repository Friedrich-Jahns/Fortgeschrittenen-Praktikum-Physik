set terminal png 
set output 'ruth_gold_fit.png'
set grid
set xlabel 'Angle[°]'
set ylabel "Countate" rotate by 90 
set logscale y

A = 0.000001
B = -5
f(x) = A/(sin(((x*2 * pi/360)-(B*2 * pi/360))/2))**4
fit f(x) "gold_data_old.dat" using 1:3:2:4 xyerrors via A, B

plot 'gold_data_old.dat' using 1:3:2:4 lc "red" ps 1 pt 7 title "Data" with xyerrorbars,\
f(x) t 'Fit' lw 1.55 lc 'black'