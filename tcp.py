#!/usr/bin/env python

import Numeric
import biggles

def congestion_window():
    yvalues = [1,2,4,8,12,13,14,15,16,1,2,4,8,9,10,11,12,13,14,1]
    return Numeric.array(range(1,len(yvalues)+1)),Numeric.array(yvalues)

def line(x1,y1,x2,y2):
    yvalues = [y1,y2]
    xvalues = [x1,x2]
    return Numeric.array(xvalues),Numeric.array(yvalues)
    
biggles.configure( 'default', 'fontface', 'Times')
p = biggles.FramedPlot()
p.aspect_ratio = 0.5
p.y1.subticks = 1
p.y2.subticks = 1
p.xlabel = 'Transmission Round'
p.ylabel = 'TCP Congestion Window'
x,y = congestion_window()
a = biggles.Curve(x,y,color="blue")
b = biggles.Points(x,y,color="blue",type="filled circle",size=1)
c = biggles.DataLine((1,12),(9,12),type="dashed")
d = biggles.DataLabel(3,12.5,"Threshold",halign="center")
e = biggles.DataLine((10,8),(19,8),type="dashed")
f = biggles.DataLine((20,7),(21,7),type="dashed")
p.add(a, b, c, d, e, f)
p.write_img(2000,1000,'tcp.png')
p.write_eps('tcp.eps')
# p.write_img(2000,1000,'tcp.gif')

