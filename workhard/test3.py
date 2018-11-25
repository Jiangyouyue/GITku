#!python2
#coding=utf-8

import os
import sys
import cairo
from PyQt4.QtCore import *
from PyQt4.QtGui import *
   
WIDTH=6000                #6000*3500
HEIGHT=3500
surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context (surface)      
ctx.set_source_rgb(0, 0, 0)     #RGB
ctx.set_line_width(1); 
'''ctx.move_to( 140,  220)
ctx.show_text("Hello World!" )
surface.write_to_png ("R3.png") '''

with open('beijingdata.txt') as f:
    data=[]
    #x=[]
    #y=[]
    for i in range(1627):          #1627
        s1=(f.readline())
        s1 = s1.rstrip('\n')
        data.append(s1.split('\t'))
        num=int(data[i][2])
        x=[]
        y=[]
        for j in range(num):
            s2=(f.readline())
            s2=s2.rstrip('\n')
            d=s2.split('\t')
            x.append(int((float(d[0])-440500)))
            y.append(int((float(d[1])-4427000)))
        ctx.move_to(x[0],y[0])
        for k in range(num-1):
            ctx.line_to(x[k+1],y[k+1])
        ctx.stroke() 
        print i  
    surface.write_to_png ("sys1.png")
    #for i,value in enumerate(x):
        #print i,value
    #for i,value in enumerate(y):
        #print i,value
    #x.sort()
    #y.sort()
    #print x[0],y[0],x[-1],y[-1]