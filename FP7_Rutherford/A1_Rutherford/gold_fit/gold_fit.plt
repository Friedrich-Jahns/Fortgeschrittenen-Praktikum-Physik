set terminal png 
set output 'ruth_gold_fit.png'
set grid
set xlabel 'Angle[°]'
set ylabel "Countate" rotate by 90 
set logscale y
set yrange [0.00007:60]

A = 0.000001
B = 4
f(x) = A/(sin(((x*2 * pi/360)-(B*2 * pi/360))/2))**4
fit f(x) "gold_data.dat" using 1:2:3:4 xyerrors via A, B

plot 'gold_data.dat' using 1:2:3:4 lc "red" ps 1 pt 7 title "Data" with xyerrorbars,\
f(x) t 'Fit' lw 1.55 lc 'black'