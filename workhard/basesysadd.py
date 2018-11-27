import math
import os
import sys
import cairo
from PIL import  Image
from PyQt4 import QtGui,QtCore


fre=900.00
noise=-174
bw=15000
rsrpl=-110
syspic1=[['sys1.png','sys2.png','sys3.png','sys4.png'],
    ['rsrp1.png','rsrp2.png','rsrp3.png','rsrp4.png'],
    ['bps1.png','bps2.png','bps3.png','bps4.png']]
WIDTH=6000                #6000*3500
HEIGHT=3500
surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context (surface)      
ctx.set_source_rgb(0, 0, 0)     #RGB
ctx.set_line_width(1); 

filename='beijingdata.txt'
with open(filename) as f:
    data=[]
    data1=[]
    xbase=[]
    ybase=[]
    rsrp=[]
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

    for i1 in range(25):          #1627
        ss=(f.readline())
        ss1=(f.readline())
        ss1 = ss1.rstrip('\n')
        ss1 = ss1.split('\t')
        x1=int((float(ss1[0])-440500))
        y1=int((float(ss1[1])-4427000))
        data1.append(ss1[2])
        xbase.append(int(ss1[0])-440500)
        ybase.append(int(ss1[1])-4427000)
        ctx.set_source_rgb(1, 0, 0)
        ctx.set_line_width(4)
        ctx.arc(x1,y1,50,0,2*math.pi)
        ctx.stroke() 
    ctx.set_source_rgb(0, 0, 0)  
    ctx.rectangle(0,0,WIDTH,HEIGHT)
    ctx.stroke()
    for i in range(600):
        for j in range(350):
            plosslis=[]
            for n in range(25):
                ht=float(data1[n])
                xlen=(xbase[n]-5-10*i)**2
                fre=float(fre)
                des=float(math.sqrt((xbase[n]-5-10*i)**2+(ybase[n]-5-10*j)**2))
                des=des/1000
                ploss=46.3+33.9*math.log10(fre)-13.82*math.log10(ht)+(44.9-6.55*math.log10(ht))*math.log10(des+0.000001)+3
                ploss=round(ploss,2)
                #noise1=10**((24.2-ploss)/10)
                #noisesum+=noise1
                plosslis.append(ploss)
            plosslis.sort()
            rsrpva=24.2-plosslis[0]
            rsrpva=round(rsrpva,2)
            #rgbsel(rsrpva,ctx)
            if rsrpva> -75 :
                ctx.set_source_rgb(0.55,0.05 ,0.55)
            else:
                ctx.set_source_rgb(0.55,0.05+round((-75-rsrpva)/70,2) ,0.55) 
            ctx.rectangle(i*10,j*10,10,10)
            ctx.fill()
            rsrp.append(rsrpva)
    rsrp.sort()
    #print xbase,ybase
    #print rsrp[0],rsrp[-1]
with open(filename) as f1:
    data=[]
    data1=[]
    for i in range(1627):          #1627
        s1=(f1.readline())
        s1 = s1.rstrip('\n')
        data.append(s1.split('\t'))
        num=int(data[i][2])
        x=[]
        y=[]
        for j in range(num):
            s2=(f1.readline())
            s2=s2.rstrip('\n')
            d=s2.split('\t')
            x.append(int((float(d[0])-440500)))
            y.append(int((float(d[1])-4427000)))
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(1)
        ctx.move_to(x[0],y[0])
        for k in range(num-1):
            ctx.line_to(x[k+1],y[k+1])
        ctx.stroke() 
    for i1 in range(25):          #1627
        ss=(f1.readline())
        ss1=(f1.readline())
        ss1 = ss1.rstrip('\n')
        ss1 = ss1.split('\t')
        x1=int((float(ss1[0])-440500))
        y1=int((float(ss1[1])-4427000))
        data1.append(ss1[2])
        ctx.set_source_rgb(1, 0, 0)
        ctx.set_line_width(4)
        ctx.arc(x1,y1,50,0,2*math.pi)
        ctx.stroke() 
surface.write_to_png ('rsrp1.png') 




'''fname='sys1.png'
    lis=[[2,2],[3,4],[4,8]]
    for i,n in lis:
        im = Image.open(fname)
        width, height = im.size
        im.thumbnail((width/n, height/n))
        im.save('sys%d.png'%i, 'png')'''
'''def rgbsel(rsrpva,ctx) :
    if ( rsrpva > 50.0 ):
        ctx.set_source_rgb(0, 1, 0) 
    elif (rsrpva<=50.0 and rsrpva > 25.0 ):
        ctx.set_source_rgb(0, 1, 0)  
    elif (rsrpva<=25.0 and rsrpva > 5.0 ):
        ctx.set_source_rgb(0, 1, 0) 
    elif (rsrpva<=-15.0 and rsrpva > -25.0 ):
        ctx.set_source_rgb(0, 1, 0) 
    elif (rsrpva<=-25.0 and rsrpva > -35.0 ):
        ctx.set_source_rgb(0, 1, 0) 
    elif (rsrpva<=-35.0 and rsrpva >-45.0 ):
        ctx.set_source_rgb(0, 1, 0) 
    elif (rsrpva<=-45.0 and rsrpva > -55.0 ):
        ctx.set_source_rgb(0, 0.9, 0) 
    elif (rsrpva<=-55.0 and rsrpva > -65.0 ):
        ctx.set_source_rgb(0, 0.8, 0) 
    elif (rsrpva<=-65.0 and rsrpva >-75.0 ):
        ctx.set_source_rgb(0, 0.7, 0) 
    elif (rsrpva<=-75.0 and rsrpva > -85.0 ):
        ctx.set_source_rgb(0, 0.6, 0) 
    elif (rsrpva<=-85.0 and rsrpva > -95.0 ):
        ctx.set_source_rgb(0.8, 0, 0) 
    elif (rsrpva<=-95.0 and rsrpva > -105.0 ):
        ctx.set_source_rgb(0.9, 0, 0) 
    else :ctx.set_source_rgb(1, 0, 0) 
        '''