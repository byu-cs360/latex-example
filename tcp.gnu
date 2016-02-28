set title ""
set xlabel "Transmission Round"
set ylabel "TCP Congestion Window"

# To make EPS:
# set term postscript color eps
# set output "tcp.eps"

# To make PNG:
set term png
set output "tcp.png"

y(x) = 12
plot "tcp.data" using 1:2 with linespoints lt 3 t "Congestion Window", \
	f(x) = (x<=10) ? 12 : (x<=20) ? 8 : 7, f(x) t "Threshold" with dots lw 1 lt -1
