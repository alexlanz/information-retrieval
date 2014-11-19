#
# In-degree distribution. G(4039, 88234). 1314 (0.3253) nodes with in-deg > avg deg (43.7), 597 (0.1478) with >2*avg.deg (Wed Nov 19 20:47:13 2014)
#

set title "In-degree distribution. G(4039, 88234). 1314 (0.3253) nodes with in-deg > avg deg (43.7), 597 (0.1478) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "In-degree"
set ylabel "Count"
set tics scale 2
set terminal png size 1000,800
set output 'inDeg.distribution.png'
plot 	"inDeg.distribution.tab" using 1:2 title "" with linespoints pt 6
