#!python2
#coding=utf-8

import random
import cairo
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
WIDTH, HEIGHT = 1200, 900
Width_per_code = 2
Height_per_code = 80  
xpos,ypos=0,0
surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context (surface)
def Numcre():             #获得随机生成的N位数字
    num=[0]
    lnum=[]
    rnum=[]
    for i in range(11):
        num.append(random.randint(0,9))
    check1 = 3 * sum(num[1::2]) + sum(num[::2])
    check2 = 10 - check1 % 10
    if check2 == 10:
        check2 = 0
    num.append(check2)
    for i in range(1,7):
        lnum.append(num[i])
    for i in range(7,13):
        rnum.append(num[i])
    return lnum,rnum
def Lcodecre(num):             #左边数字转义函数
    code=''
    for i in range(len(num)):
        code+=dict_lcode[num[i]]
    return code
def Rcodecre(num):              #右边数字转义函数
    code=''
    for i in range(len(num)):
        code+=dict_rcode[num[i]]
    return code   
class Drawcode(object):     #画图父类
    
    def __init__(self, ctx):
        self.ctx=ctx
    def draw(self, code):
        global xpos,ypos
        ctx.move_to(xpos,ypos)
        ctx.set_source_rgb(0, 0, 0)
        for i,c in enumerate(code):
            xpos += Width_per_code 
            if c=='1' :
                ctx.rectangle(xpos,ypos,Width_per_code,Height_per_code)
                ctx.fill()
        xpos += Width_per_code
class LeftRightGuard(Drawcode):
    def __init__(self):
        super(LeftRightGuard, self).__init__(ctx)
class CenterGuard(Drawcode):
    def __init__(self):
        super(CenterGuard, self).__init__(ctx)
class Leftcode(Drawcode):
    
    def draw(self):
        global lnum
        lcode=Lcodecre(lnum)
        global xpos,ypos
        ctx.move_to(xpos,ypos)
        ctx.set_source_rgb(0, 0, 0)
        for i,c in enumerate(lcode):
            xpos += Width_per_code 
            if c=='1' :
                ctx.rectangle(xpos,ypos,Width_per_code,Height_per_code-20)
                ctx.fill()
            if i%7==0:
                ctx.move_to(xpos,ypos+Height_per_code)
                ctx.set_font_size(16)
                ctx.show_text("%s"%lnum[i/7])
        xpos += Width_per_code
class Rightcode(Drawcode):
    
    def draw(self):
        global rnum
        rcode=Rcodecre(rnum)
        global xpos,ypos
        ctx.move_to(xpos,ypos)
        ctx.set_source_rgb(0, 0, 0)
        for i,c in enumerate(rcode):
            xpos += Width_per_code 
            if c=='1' :
                ctx.rectangle(xpos,ypos,Width_per_code,Height_per_code-20)
                ctx.fill()
            if i%7==0:
                ctx.move_to(xpos,ypos+Height_per_code)
                ctx.set_font_size(16)
                ctx.show_text("%s"%rnum[i/7])
        xpos += Width_per_code
def create():
    s=Drawcode(ctx)
    l=Leftcode(ctx)
    r=Rightcode(ctx)
    lrg=LeftRightGuard()
    cg=CenterGuard()
    lrg.draw("101")
    l.draw()
    cg.draw("01010")
    r.draw()
    lrg.draw("101")
for i in (0,1,2):
    for j in (0,1,2,3):
        xpos=100+320*i
        ypos=100+200*j
        lnum,rnum=Numcre()
        create()
surface.write_to_png("code4.png")


   