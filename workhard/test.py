#!python2
#coding=utf-8
import math
import random
import string
import cairo
'''
left_guard = "101"
right_guard = "101"
centerguard = "0101"
dict_lcode = {
 0: "0001101",
 1: "0011001",
 2: "0010011",
 3: "0111101",
 4: "0100011",
 5: "0110001",
 6: "0101111",
 7: "0111011",
 8: "0110111",
 9: "0001011"
}
dict_rcode = {
 0: "1110010",
 1: "1100110",
 2: "1101100",
 3: "1000010",
 4: "1011100",
 5: "1001110",
 6: "1010000",
 7: "1000100",
 8: "1001000",
 9: "1110100"
}
def Numcre():
    num=[]
    lnum=[]
    code=''
    for i in range(12):
        num.append(random.randint(0,9))
    check1 = 3 * sum(num[1::2]) + sum(num[::2])
    check2 = 10 - check1 % 10
    if check2 == 10:
        check2 = 0
    num.append(check2)
    for i in range(1,7):
        lnum.append(num[i])
    return num,lnum
m,n=Numcre()
print m,n
WIDTH, HEIGHT = 600, 300
Width_per_code = 10
Height_per_code = 200
code =[0,1,0,1,0]
surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context (surface)
ctx.translate(50,50)
ctx.set_source_rgb(0, 0, 0)
for i,c in enumerate("01010"):
    xpos = Width_per_code *i
    if c=='0' :
        ctx.rectangle(xpos,0,Width_per_code,Height_per_code)
        ctx.fill()
surface.write_to_png("3.png")
surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, 100, 100)
ctx = cairo.Context (surface)
ctx.set_source_rgb(0, 0, 0)
ctx.arc(50,50,10,0,2*math.pi)
ctx.stroke()
surface.write_to_png("code6.png")'''
print "为什么："
print "1"

a="中文"
print(a.decode("utf-8").encode("gbk"))